#!/usr/bin/python3
# encoding: utf-8
"""A setuptools based setup module for run_web_pycode"""

from codecs import open
from os import path

from setuptools import find_packages, setup

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open(path.join(here, "HISTORY.md"), encoding="utf-8") as history_file:
    history = history_file.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as requirements_file:
    requirements = requirements_file.read()

with open(path.join(here, "requirements_dev.txt"), encoding="utf-8") as requirements_dev_file:
    requirements_dev = requirements_dev_file.read()

ext_modules = []
setup(
    name="run_web_pycode",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A package to execute remote python scripts",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="AngusWG",
    author_email="740713651@qq.com",
    url="https://github.com/AngusWG/run-web-pycode",
    packages=find_packages(include=["run_web_pycode", "run_web_pycode.*"]),
    entry_points={
        "console_scripts": [
            "run_web_pycode=run_web_pycode.__main__:entry_point",
            "pyw=run_web_pycode.__main__:entry_point",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={"dev_require": requirements + "\n" + requirements_dev},
    ext_modules=ext_modules,
    keywords="run_web_pycode",
)
