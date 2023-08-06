from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'An Automated EIS analysis packgae'
LONG_DESCRIPTION = 'A package to perform fully automated EIS analysis based on equivalent circuit models'

# Setting up
setup(
    name="AutoEis",
    version= VERSION,
    author="Runze zhang, Robert Black, Parisa Karimi, Jason Hattrick-Simpers*",
    author_email="runzee.zhang@mail.utoronto.ca",
    description= DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="",
    packages = find_packages(),
    install_requires = ['matplotlib>=3.3.2',
                        'numpy>=1.20.3',
                        'json>=2.0.9',
                        'pandas>=1.1.3',
                        'impedance>=1.4.0',
                        'regex>=2.2.1',
                        'arviz>=0.12.0',
                        'numpyro>=0.9.1',
                        'dill>=0.3.4',
                        'julia>=0.5.7',
                        'IPython>=7.19.0'],
    keywords=['python', 'Electrochemical impedance spectroscopy', 'Fully-automated', 'equivalent circuit models', 'gene-expression programming', 'genetic algorithm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
)
