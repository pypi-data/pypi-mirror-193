"""
Quirk to guarantee correct Pythonpath and single source of truth versioning
"""
from importlib.metadata import version, PackageNotFoundError
__author__ = """Henrik Stromberg"""
__email__ = 'henrik@askdrq.com'
try:
    __version__ = version('simtwin')
except PackageNotFoundError:
    __version__ = '0.0.0'
