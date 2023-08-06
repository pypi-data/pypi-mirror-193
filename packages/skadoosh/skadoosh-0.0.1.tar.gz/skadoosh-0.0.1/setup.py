import os

from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))

long_description = open(os.path.join(HERE, 'README.md'), 'r', encoding='utf8').read()
setup(
    name='skadoosh',
    version='0.0.1',
    description='Skadoosh python package',
    long_description=long_description,
    author='Nguyen Trieu',
    author_email='tdnguyen.uet@gmail.com',
    packages=['skadoosh'],
    install_requires=[
    ],
)
