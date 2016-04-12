try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Category Module for Laptop Cases',
    'author': 'Kirthanaa Raghuraman',
    'url': '',
    'download_url': '',
    'author_email': 'kirthanaa@cs.wisc.edu',
    'version': '0.1',
    'install_requires':['simplejson'],
    'packages': ['CategoryModule_LaptopCase'],
    'scripts': [],
    'name': 'categoryModule'
}

setup(**config)
