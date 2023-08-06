from .snake_wrapper import SnakEcdysis, SnakeInstaller
from .cli_wrapper import main_wrapper
from .useful_function import *
from setuptools_scm import get_version

__version__ = get_version(version_scheme="no-guess-dev", local_scheme="no-local-version", tag_regex=r"^(\d.\d.\d-*\w*\d*)$")

__doc__ = """
You want to wrap your best snakemake workflow to be easy install and run, Snakecdysis is for you !!!!!
Tha aim of Snakecdysis is to easy-wrapped snakemake workflow as python package and then build sub-commands to manage this.
"""
