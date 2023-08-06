"""
Python setup file for the unsupported package.

For more information on creating source distributions, see
http://docs.python.org/3/distutils/sourcedist.html
"""
import os
from setuptools import find_packages, setup
import psu_export as app


# Function for reading the contents of a file
def read(filename):
    try:
        return open(os.path.join(os.path.dirname(__file__), filename)).read()
    except IOError:
        return ''


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='psu_export',
    version=app.__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Unsupported',
    long_description="Unsupported code. ",
    long_description_content_type="text/markdown",
    url='https://www.pdx.edu',
    author='PSU',
    author_email='roreply@pdx.edu',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=read('requirements.txt').splitlines()
)
