from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'topsisGod',
    version = '0.0.4',
    description = 'Calculation of Topsis Score',
    py_modules = ['topsisGod'],
    package_dir = {'':'src'},
    classifiers=[
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type = "text/markdown",
    author="Sahil Chhabra",
    author_email="sahil.chh718@gmail.com",
)