
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(description= 'Predicts match based on variation',
    author='Arjun Gurumurthy',
    url= '',
    download_url= '',
    author_email= 'arjun@cs.wisc.edu',
    version= '1.0',
    install_requires=['simplejson'],
    packages= ['variation_module'],
    scripts= [],
    name= 'variation_module'
)
