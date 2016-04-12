__author__ = 'kavin'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Weight Matcher',
    'author': 'Kavin Mani',
    'author_email': 'kavin@cs.wisc.edu',
    'version': '1.0',
    'url':'',
    'download_url':'',
    'install_requires': ['simplejson'],
    'packages': ['weight_module'],
    'scripts': [],
    'name': 'weight_module'
}

setup(**config)
