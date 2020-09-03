# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lambdadata_yinmialas", # the name that you will install via pip
    version="2.0",
    author="Yinmi Alas",
    author_email="jimmyalas73@gmail.com",
    description="my def function package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/YinmiAlas/lambdadata-yinmialasdspt7",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
    )