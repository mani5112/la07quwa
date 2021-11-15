from distutils.core import setup
from setuptools import find_packages
setup(name='la07quwa',
      version='0.1',
      author='DSSS',
      author_email='manikanta.rajoli@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])