from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'NokiaLCD',
	  version 			= '1.0.0',
	  author			= 'SourcExplained (Kabe)',
	  author_email		= 'sourcexplained@gmail.com',
	  description		= 'Library to display text and images on the Nokia 5110/3110 LCD.',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/Adafruit_Nokia_LCD/',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.1.0'],
	  install_requires	= ['Adafruit-GPIO>=0.1.0', 'PIL'],
	  packages 			= find_packages())
