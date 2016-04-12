__author__ = 'neha'

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Height/Length/Width Matcher',
	'author': 'Neha Godwal',
	'author_email': 'nhgodwal@gmail.com',
	'version': '1.0',
	'url':'',
	'download_url':'',
	'install_requires': ['simplejson'],
	'packages': ['HeightLengthWidth_module'],
	'scripts': [],
	'name': 'HWL_module'
	}

setup(**config)
