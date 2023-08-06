from setuptools import setup

setup(
    name='ocrmymanga',
    version='0.14',
    description='A handy tool for OCRing manga',
    packages=['OCRMyManga'],
    install_requires=[
        # List any dependencies your package requires
        'requests',
        'pillow',
        'reportlab',
        'PyPDF2',
        'google-cloud-vision',
    ],
    entry_points={
        'console_scripts': [
            # If your package includes a command-line interface, you can define it here
            'ocrmymanga = OCRMyManga.__init__:main',
        ],
    },
    long_description=open('README.md').read(),
)
