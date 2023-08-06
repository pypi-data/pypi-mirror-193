from setuptools import setup, find_packages

from wjec_utils_package import __version__

setup(
    name='wjec_utils_package',
    version=__version__,
    copyright='Weir-Jones Ltd',
    author='Cathal D',
    packages=find_packages()
)