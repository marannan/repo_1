
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Brand name matcher',
    'author': 'Ali Hussain Hitawala',
    'url': 'profile.alihitawala.com',
    'download_url': '',
    'author_email': 'alihitawala@cs.wisc.edu',
    'version': '0.1',
    'install_requires': ['nose', 're', 'logging', 'editdistance', 'json'],
    'packages': ['brand_module'],
    'scripts': [],
    'name': 'brandNameModule'
}

setup(**config)
