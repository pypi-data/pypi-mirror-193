import setuptools
from pathlib import Path

setuptools.setup(
    name='anandpdf',
    version=1.0,
    long_description=Path('./REEDME.md').read_text(),
    packages=setuptools.find_packages(exclude=['setup.py', 'data'])

)
