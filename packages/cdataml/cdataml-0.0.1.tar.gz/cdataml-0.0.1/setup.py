from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'CDA Data for Machine Learning'

# Setting up
setup(
    name="cdataml",
    version=VERSION,
    author="Joshua Williams",
    author_email="<jowillia@nbi.ac.uk>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python'],
    keywords=['python', 'plant pathology', 'cell death', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
