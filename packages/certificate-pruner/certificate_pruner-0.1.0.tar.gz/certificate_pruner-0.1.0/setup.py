from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
name="certificate_pruner",
version="0.1.0",
author="Soriyath Straessle",
author_email="soriyath@leading.works",
description="Prune SSL certificate from a Let's Encrypt JSON file",
long_description="This script prunes a JSON file containing Let's Encrypt certificates. It removes one of the certificates and saves the pruned content to a new file.",
long_description_content_type="text/markdown",
url="https://gitlab.com/leading-works/devops",
packages=find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
"Operating System :: OS Independent",
],
python_requires='>=3.6',
install_requires=[]
)
