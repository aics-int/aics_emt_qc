# -*- coding: utf-8 -*-

"""Top-level package for emt_qc."""

from .emt_block_duration import (
    emt_block_duration,
    pipeline_tools,
)

__author__ = "Brian Whitney"
__email__ = "brian.whitney@alleninstitute.org"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.0.0"


def get_module_version():
    return __version__
