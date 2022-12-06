# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import warnings
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))
master_doc = 'index'
add_module_names = False

def setup(app):
    app.add_css_file(os.path.join("css","custom.css"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mapstatic'
copyright = '2022, Thiziri Abchiche, Rim Alhajal, Maryem El Yamani, Lilou Zulewski'
author = 'Thiziri Abchiche, Rim Alhajal, Maryem El Yamani, Lilou Zulewski'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
pygments_style = 'monokai'
html_static_path = ['_static']
html_logo = '_static/mapstaticlogo.svg'
