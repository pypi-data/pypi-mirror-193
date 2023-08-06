from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.2'
DESCRIPTION = 'Country library'
LONG_DESCRIPTION = 'A package that allows to get country information like official name, population and so on...'

# Setting up
setup(
    name="countrylibrary",
    version=VERSION,
    author="Abraham",
    author_email="ibrohimjon.ismoilov.007@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['httpx'],
    keywords=['python', 'country', 'information', 'country information', 'population', 'area of countries'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
