import datetime

# -- Project information -----------------------------------------------------

html_title = 'Visualization with Python'
project = "Matplotlib cheatsheets"
copyright = (
    f"2012 - {datetime.datetime.now().year} The Matplotlib development team"
)
author = "Matplotlib Developers"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.

templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_css_files = ['css/normalize.css', 'css/landing.css']
html_theme = "mpl_sphinx_theme"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "logo_link": "https://matplotlib.org/stable/",
    "native_site": False,
}
html_sidebars = {
    "**": []
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the theme static files,
# so a file named "default.css" will overwrite the theme's "default.css".
html_static_path = ["_static"]
