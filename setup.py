from setuptools import setup
from setuptools import find_packages

setup (
    name="my_package",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requires =["numpy"],
    url="https://github.com/<username>/<package-name>",
    author="McMunashe",
    author_email="mcmunashemunemo1@gmail.com"
)