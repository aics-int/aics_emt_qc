#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import find_packages, setup

requirements = [
    "aicsimageio ~= 4.4",
    "aicspylibczi ~= 3.0.0",
    "numpy ~= 1.21",
    "scikit-image ~= 0.18",
]

dev_requirements = [
    # Test
    "black == 22.1.0",
    "flake8 ~= 4.0.1",
    "isort ~= 5.10.1",
    "mypy ~= 0.910",
    "pytest ~= 6.2.5",
    "pytest-raises ~= 0.11",
    # Dev workflow
    "pre-commit ~= 2.17.0",
    # Build
    "build == 0.7.0",
    # Version
    "bump2version ~= 1.0.1",
    # Publish
    "twine ~= 3.7.1",
    # Documentation generation
    "Sphinx ~= 4.4.0",
    "furo == 2022.1.2",  # Third-party theme (https://pradyunsg.me/furo/quickstart/)
    "m2r2 ~= 0.3.2",  # Sphinx extension for parsing README.md as reST and including in Sphinx docs
]

extra_requirements = {
    "dev": dev_requirements,
}


def readme():
    with open("README.md") as readme_file:
        return readme_file.read()


setup(
    author="Brian Whitney",
    author_email="brian.whitney@alleninstitute.org",
    description="Contains pipeline functions for pipeline 8 (EMT)",
    install_requires=requirements,
    extras_require=extra_requirements,
    entry_points={
        "console_scripts": [
            "emt_block_duration=emt_qc.bin.emt_block_duration:main",
        ],
    },
    license="Allen Institute Software License",
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="aics_emt_qc",
    name="aics_emt_qc",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.9",  # This is driven by aicsimageio constraints
    url="https://github.com/BrianWhitneyAI/aics_emt_qc",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="1.0.0",
    zip_safe=False,
)
