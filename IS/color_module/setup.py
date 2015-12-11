
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(description= 'Predicts match based on color attribute',
    author='Ashok Marannan',
    url= '',
    download_url= '',
    author_email= 'ashok.marannan@hotmail.com',
    version= '1.0',
    install_requires=['simplejson'],
    packages= ['color_module'],
    scripts= [],
    name= 'color_module'
)
