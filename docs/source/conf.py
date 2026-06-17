import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

project = 'Firma Fotografía'
author = 'Luis Villagra'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    "sphinx_wagtail_theme"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# html_theme = 'sphinx_rtd_theme'

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
# html_last_updated_fmt = '%b %d, %Y'

# autodoc_member_order = 'bysource'
# autodoc_typehints = 'description'
