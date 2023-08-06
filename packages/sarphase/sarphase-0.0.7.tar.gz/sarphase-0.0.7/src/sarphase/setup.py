from setuptools import setup

exec(open("sarphase/_version.py").read())

setup(
    version=__version__)