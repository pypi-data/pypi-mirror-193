from setuptools import setup, find_packages
from os.path import join, dirname
import hesl

setup(
    name='hesl',
    version=hesl.__version__,
    author='LowLevelCoder',
    author_email='flat.assembly@gmail.com',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts': ['heslc = hesl.core:compile']
    },
    test_suite='tests',
)
