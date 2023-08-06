from setuptools import setup, find_packages

setup(
    name="cdataml",
    version='0.0.3',
    author="Joshua Williams",
    author_email="<jowillia@nbi.ac.uk>",
    description='CDA Data for Machine Learning',
    long_description='Package to build CDA Data for use in Machine Learning algorithms',
    packages=find_packages(),
    install_requires=['opencv-python', 'pandas', 'natsort'],
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
