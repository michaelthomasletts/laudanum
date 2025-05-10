import os
import sys
from datetime import date
from pathlib import Path

import tomlkit

# fetching pyproject.toml
path = Path("../pyproject.toml")

with path.open("r", encoding="utf-8") as f:
    pyproject = tomlkit.parse(f.read())

# sphinx config
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))
extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.linkcode",
    "sphinx.ext.extlinks",
    "sphinx_click.ext",
]
language = "en"
project = str(pyproject["project"]["name"])
author = "Mike Letts"
copyright = f"{date.today().year}, {author}"
release = str(pyproject["project"]["version"])
source_encoding = "utf-8"
source_suffix = ".rst"
pygments_style = "sphinx"
add_function_parentheses = False
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "tests/"]
# html_logo = "laudanum.png"
# html_favicon = html_logo
html_title = project
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_file_suffix = ".html"
html_sidebars = {
    "**": [],
}
html_context = {
    "default_mode": "dark",
}
htmlhelp_basename = project
html_css_files = ["custom.css"]
html_theme_options = {
    "collapse_navigation": True,
    "navbar_end": [
        "search-button",
        "navbar-icon-links.html",
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": f"https://github.com/michaelthomasletts/{project}",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": f"https://pypi.org/project/{project}/",
            "icon": "fab fa-python",
            "type": "fontawesome",
        },
    ],
}

# autodoc config
autodoc_default_options = {
    "members": True,
    "member-order": "alphabetical",
    "exclude-members": "__init__",
}
autodoc_typehints = "none"
autodoc_preserve_defaults = False
autodoc_class_signature = "separated"
add_module_names = False

# numpydoc config
numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False
numpydoc_attributes_as_param_list = False
numpydoc_class_members_toctree = False

# napoleon config
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False

# autosummary
generate_autosummary = True


def linkcode_resolve(domain, info):
    """Resolves 'source' link in documentation."""

    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return f"https://github.com/michaelthomasletts/{project}/blob/main/{filename}.py"