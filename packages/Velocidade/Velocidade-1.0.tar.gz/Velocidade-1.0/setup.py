from setuptools import find_packages,setup
from pathlib import Path


setup(
    nome='test-velocimetro',
    version=1.0,
    description='esse pacote não faz absolutamente nada',
    long_description=Path('Readme.md').read_text(),
    author='KLenine',
    author_email='nono@gmail.com',
    keywords=['nem','pilha','nisso'],
    packages=find_packages()
) 