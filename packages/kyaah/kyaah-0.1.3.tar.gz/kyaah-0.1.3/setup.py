# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
from kyaah import (__title__, __version__, __author__, __author_email__, __repository__, __website__)


setup(
  
  # name of the main package (base dir)
  name=__title__,
  version=__version__,
  description="**Kyaah** abstract away SMTP mail operations complexity",
  long_description=open("README.md").read() + "\n\n" + open("CHANGELOG").read(),
  long_description_content_type="text/markdown",
  python_requires='>=3.6',
  
  # The URL of your package's (project) home page e.g. github link
  url=__website__,
  repo=__repository__,
  author=__author__,
  author_email=__author_email__,
  License="MIT",
  
  classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
  ],
  
  # used when people are searching for a module, keywords separated with a space
  keywords="kyaah",
  
  # The list of packages(directories) for your library
  packages=find_packages(), # OR packages=["kyaah"] 
  # If your package is a single module, use this instead of "packages":
  # py_modules=[""] # list of files (modules) that are not in any directory (at the root dir)
  # the libraries it depends on
  
  include_package_data = True, # include files listed in MANIFEST.in
  
  # List of other python modules which this module depends on.  For example RPi.GPIO
  install_requires=["geocoder==1.38.1"]
)
