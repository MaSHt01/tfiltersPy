import os
import sys
sys.path.insert(0, os.path.abspath('../'))

try:
    # For Python 3.8 and above
    from importlib.metadata import version
except ImportError:
    # For older versions of Python, use the backport
    from importlib_metadata import version

# Set the release variable dynamically using the package version.
release = version("tfilterspy")

# -- Project information -----------------------------------------------------
project = 'tfilters'
copyright = (
    '2025, Thabang Mashinin-Sekhoto, '
    'Lebogang Mashinini-Sekhoto, '
    'Palesa Mashinini-Sekhoto'
)
author = 'Thabang Mashinin-Sekhoto, Lebogang Mashinini-Sekhoto, Palesa Mashinini-Sekhoto'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',           # Automatically document modules
    'sphinx.ext.napoleon',          # Support for Google/NumPy-style docstrings
    'sphinx.ext.autodoc.typehints', # Add type hints to the documentation
    'sphinx.ext.viewcode',          # Link source code in the docs
    'nbsphinx',                    # Renders Jupyter notebooks
]
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
