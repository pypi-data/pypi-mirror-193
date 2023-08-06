# https://www.freecodecamp.org/news/build-your-first-python-package/
from setuptools import setup, find_packages

VERSION = '1.5' 
DESCRIPTION = 'Extract data from files in python'
LONG_DESCRIPTION = '''
A python package for extracting data from files, more on github.

          https://github.com/itzCozi/Data-Extraction
'''

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="Data Extract", 
        version=VERSION,
        author="Cooper ransom",
        author_email="Cooperransom08@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'data', 'extraction', 'list'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
