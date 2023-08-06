from setuptools import setup
from setuptools import find_packages

setup(
    name='RS_project',
    version='0.1',
    description='My first PyPI project',
    author = 'Stelian, Radu',
    author_email = 'stlnradu@gmail.com',
    install_requires=[
        'pandas',
        'numpy',
        #TBC
    ],
    packages=find_packages(),
    include_package_data=True)