# src/strutils/__init__.py
# flake8: noqa
"""(compound) STRing UTILitieS. Rudimentary, outdated, everywhere else found."""
from importlib.metadata import version

from .core import permute_splits, sos_on, variate_compounds

__version__ = version(__name__)
