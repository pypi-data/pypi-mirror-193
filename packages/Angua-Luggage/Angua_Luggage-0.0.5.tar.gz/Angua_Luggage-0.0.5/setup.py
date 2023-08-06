# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:19:59 2023

@author: mwodring
"""

from setuptools import setup, find_packages

VERSION = '0.0.5' 
DESCRIPTION = 'Additional commands for Angua and other Bioinformatic tools.'
LONG_DESCRIPTION = 'Additional commands for Angua and other Bioinformatic tools.'

# Setting up
setup(
        package_data={'data': ['/data/']},
        include_package_data=True,
	scripts = ["bin/rma.py", "bin/TextSearch.py", "bin/getORFs.py", "bin/fetchSRA.py", "bin/ICTVEntrez.py"],
        name="Angua_Luggage", 
        version=VERSION,
        author="Morgan Wodring",
        author_email="morgan.wodring@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["Bio", "rpy2"],
        #Note: Make a requirements file for the Angua env after all is said and done.
        keywords=['bioinformatics', 'angua'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3"
        ]
)