from setuptools import setup, find_packages
import codecs
import os

VERSION = "1.0.0"
DESCRIPTION = "A simple python package that allows to get zeroshot labels and build a classifier."
LONG_DESCRIPTION = "A simple python package that allows to get zeroshot labels and build a classifier."

# Setting up
setup(
    name="lazy-nlp",
    version=VERSION,
    author="Leonard Püttmann",
    author_email="<leopuettmann@outlook.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["transformers", "torch", "numpy", "scikit-learn", "sentence_transformers"],
    keywords=["python", "zeroshot", "nlp", "lazy-nlp"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)