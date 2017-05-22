# -*- coding: utf-8 -*-

from setuptools import setup

import kwconfig as package

def readme():
  with open('README.rst') as f:
    for i in range(11):
      next(f)
    return f.read()[1:]
        
setup(
  name=package.__name__,
  version=package.__version__,
  description=package.__description__,
  long_description=readme(),
  author=package.__author__,
  author_email=package.__email__,
  license=package.__license__,
  url=package.__url__,
  download_url=package.__download_url__,
  keywords =package. __keywords__
)
