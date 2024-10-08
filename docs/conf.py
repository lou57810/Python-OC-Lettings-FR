# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
# import pathlib


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
sys.path.insert(0, os.path.abspath("../"))
# sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
# sys.path.insert(1, os.path.abspath("."))
# sys.path.insert(1, "/oc_lettings_site/")
# sys.path.insert(1, "/lettings/")
# sys.path.insert(1, "/profiles/")
# sys.path.insert(1, os.path.abspath('.'))
# sys.path.insert(1, os.path.abspath('./'))
# sys.path.insert(1, os.path.abspath('../'))
# sys.path.insert(1, os.path.abspath('../../'))

project = 'Python-OC-Lettings-FR'
copyright = '2024, Ben_Oc'
author = 'Ben_Oc'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.duration",
              "sphinx.ext.doctest",
              "sphinx.ext.autodoc",
              "sphinx.ext.viewcode",
              "sphinx.ext.napoleon"
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.png'
