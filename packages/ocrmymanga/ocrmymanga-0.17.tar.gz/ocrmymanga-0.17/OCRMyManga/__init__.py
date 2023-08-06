from PIL import Image
from zipfile import ZipFile
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
import reportlab.rl_config
from PyPDF2 import PdfMerger
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from io import BytesIO
import argparse
from enum import Enum
import io
import os
from pprint import pprint

from google.cloud import vision
from PIL import Image, ImageDraw
import sys


class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon(
            [
                bound.vertices[0].x,
                bound.vertices[0].y,
                bound.vertices[1].x,
                bound.vertices[1].y,
                bound.vertices[2].x,
                bound.vertices[2].y,
                bound.vertices[3].x,
                bound.vertices[3].y,
            ],
            None,
            color,
        )
    return image


def get_document_bounds(image_file, feature):
    document = getAnnotations(image_file)

    bounds = []

    # Collect specified feature bounds by enumerating all document features
    # Lmao this is so hacky
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if feature == FeatureType.SYMBOL:
                            bounds.append(symbol.bounding_box)

                    if feature == FeatureType.WORD:
                        bounds.append(word.bounding_box)

                if feature == FeatureType.PARA:
                    bounds.append(paragraph.bounding_box)

            if feature == FeatureType.BLOCK:
                bounds.append(block.bounding_box)

    # The list `bounds` contains the coordinates of the bounding boxes.
    return bounds


def getAnnotations(image_file):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    # Convert to io byte format
    buffer = io.BytesIO()
    image_file.save(buffer, format="PNG")

    image = vision.Image(content=buffer.getvalue())

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document


def render_doc_text(filein, fileout):
    image = Image.open(filein)
    render_doc_text_fromimg(image, fileout)


def render_doc_text_fromimg(img, fileout):
    bounds = get_document_bounds(img, FeatureType.BLOCK)
    draw_boxes(img, bounds, "blue")
    bounds = get_document_bounds(img, FeatureType.PARA)
    draw_boxes(img, bounds, "red")
    bounds = get_document_bounds(img, FeatureType.WORD)
    draw_boxes(img, bounds, "yellow")

    if fileout != 0:
        img.save(fileout)
    else:
        img.show()


def get_doc_metadata(img):
    annotations = getAnnotations(img)

    return annotations


# Execution sandbox
# Create a pdf with the img as background

# render_doc_text("resources/ocrtest2.png", "out/doc_ocr_out.png")

reportlab.rl_config.warnOnMissingFontGlyphs = 0

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))


def imgToPdf(img, pdf_merger, alpha=0.0):

    annotations = get_doc_metadata(img)

    # Create in-memory PDF files
    pdf_buffer = BytesIO()
    can = canvas.Canvas(pdf_buffer)
    fontSize = 16
    can.setFont('HeiseiMin-W3', fontSize)

    # Also throw the image onto the canvas
    imgReader = ImageReader(img)

# Write img to the canvas (stretch to fill page)
    can.drawImage(imgReader, 0, 0, can._pagesize[0], can._pagesize[1])
    textObj = can.beginText(0, 0)
    textObj.setFillColor('black', alpha=alpha)

    for (i, page) in enumerate(annotations.pages):
        # Just gonna assume we're on page 1 here with the request
        for (j, block) in enumerate(page.blocks):
            for (k, paragraph) in enumerate(block.paragraphs):
                # Get paragraph text
                for (l, word) in enumerate(paragraph.words):
                    for (m, symbol) in enumerate(word.symbols):
                        text = symbol.text

                        # Draw paragraph text
                        poly = symbol.bounding_box.vertices
                        coords = [(p.x, img.size[1]-p.y) for p in poly]

                        # First quadrant
                        # coords = [(p.x, p.y) for p in poly]

                    # Coords are currently image-size, convert to pdf-size
                        pdf_coords = [(p[0] * can._pagesize[0] / img.size[0],
                                       p[1] * can._pagesize[1] / img.size[1]) for p in coords]

                        # Width is height, square characters (get dist between corners)
                        charDims = pdf_coords[1][0] - pdf_coords[0][0]
                        fontScale = charDims / fontSize

                        # Move pointer to where the char should be
                        minx = min([p[0] for p in pdf_coords])
                        maxy = max([p[1] for p in pdf_coords])
                        desiredPos = (minx, maxy - charDims)

                        # Set font to scale with char height
                        textObj.setTextTransform(
                            fontScale, 0, 0, fontScale, desiredPos[0], desiredPos[1])
                        # textObj.setTextTransform(textObj.getX(), textObj.getY(), 1, 1, 1 ,1)

                        textObj.textOut(text)
    can.drawText(textObj)

    # Test draw string
    # can.drawString(100, 100, "你好")
    # can.drawString(130, 100, "你好")

    # Save PDF file
    can.save()
    pdf_buffer.seek(0)

    # Merge PDF files
    pdf_merger.append(pdf_buffer)

# File end checker


def validFileType(input_file):
    return input_file.endswith(('.png', '.jpg', '.jpeg', '.cbz'))


def logVerbose(message, verboseOnly=False):
    if (verboseOnly and not verbose):
        return
    print(message)


def inputFileToPdf(input_file, output_file, alpha=0.0):

    logVerbose("Beginning job for file: " + input_file)
    logVerbose("Output file: " + output_file, True)
    logVerbose("Text alpha: " + str(alpha), True)

    # Get file type
    tail = os.path.splitext(input_file)[1]

    imgs = []

    if (tail == ".cbz"):
        with ZipFile(input_file, 'r') as zip:
            nameList = zip.namelist()

            # Lexicographic sort
            nameList.sort()

            for name in nameList:

                if name.endswith('.jpg') or name.endswith('.png'):
                    with zip.open(name) as file:
                        img_data = io.BytesIO(file.read())
                        img = Image.open(img_data)
                        imgs.append({"img": img, "name": name})

                        logVerbose("Added image to queue: " + name, True)

    else:
        imgs.append({"img": Image.open(input_file), "name": input_file})

    # Create a pdf merger
    pdf_merger = PdfMerger()

    # Convert the input file to a pdf
    for img in imgs:
        imgToPdf(img["img"], pdf_merger, alpha)
        logVerbose("Printed image to pdf: " + img["name"], True)

    # Write the pdf to the output file
    with open(output_file, 'wb') as fout:
        pdf_merger.write(fout)


verbose = False


# Main function
def main():
    parser = argparse.ArgumentParser(description='OCRs Manga files')

    # Argument for input file/dir, batch processing flap, output file/dir, and text alpha
    parser.add_argument('input', type=str,
                        help='Input file or directory')
    parser.add_argument('-b', '--batch', action='store_true',
                        help='Batch process input directory')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file or directory')
    parser.add_argument('-a', '--alpha', type=float,
                        default=0.0,
                        help='The alpha of the text overlay')
    parser.add_argument('-v', '--verbose',
                        action='store_true', help='Verbose output')
    parser.add_argument('-c', '--credentials', type=str,
                        help='Path to credentials.json file (if not in same directory as script or not named credentials.json)')

    args = parser.parse_args()

    # Get the input file/dir, output file/dir, and alpha
    input = args.input
    output = args.output
    alpha = args.alpha
    verbose = args.verbose
    creds = args.credentials

    if (creds == None):
        creds = 'credentials.json'

    # Setup creds
    if (os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') == None):
        if not os.path.exists(creds):
            print(
                f"Credentials file not found. Please place {creds} in your working directory or specify the path to the credentials file with the -c flag")
            print("This tool uses Google Cloud Vision API")
            print(
                "See https://cloud.google.com/vision/docs/setup for info on acquiring your credentials file")
            print("Alternatively, you can set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your credentials file.")

            sys.exit(1)

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = creds

    if (input == None):
        print("Input file/directory not specified")
        sys.exit(1)

    if (output == None):

        # Trim off end and add _ocr.pdf
        output = input[:input.rfind('.')] + '_ocr.pdf'

    if (alpha == None):
        alpha = 0.0

    # Check if input file/dir exists
    if not os.path.exists(input):
        print("Input file/directory does not exist")
        sys.exit(1)

    # Check if batch processing
    if args.batch:
        # Check if input is a directory
        if not os.path.isdir(input):
            print("Input file is not a directory")
            sys.exit(1)

        # Check if output is a directory
        if os.path.exists(output) and not os.path.isdir(output):
            print("Output file is not a directory")
            sys.exit(1)

        # Make the output directory if it doesn't exist
        if not os.path.exists(output):
            os.mkdir(output)

        # Get the list of files in the input directory
        input_files = os.listdir(input)

        # Iterate over the input files and convert them
        for input_file in input_files:
            # Get the input folder path
            input_file_path = os.path.join(input, input_file)

            # Get the output folder path
            output_fname = input_file[:input_file.rfind('.')] + '_ocr.pdf'
            output_file_path = os.path.join(output, output_fname)

            # Check if the input file is an image (check for .png or .jpg or .jpeg)
            if not validFileType(input_file):
                continue

            # Convert the file
            inputFileToPdf(input_file_path, output_file_path, alpha=alpha)
    else:
        # Check if output is a valid file path
        if os.path.exists(output) and os.path.isdir(output):
            print("Output file is not a file")
            sys.exit(1)

        if not validFileType(input):
            print("Input file is not a valid file type")
            sys.exit(1)

        # Convert the file
        inputFileToPdf(input, output, alpha)

    print("Task completed")


if (__name__ == "__main__"):
    main()
