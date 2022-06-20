# -*- coding: utf-8 -*-

# Authors:
#   Unai Martinez-Corral
#
# Copyright 2022 Unai Martinez-Corral <unai.martinezcorral@ehu.eus>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0


from sys import path as sys_path
from os.path import abspath
from pathlib import Path
from json import loads

ROOT = Path(__file__).resolve().parent

sys_path.insert(0, abspath("."))

# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
}

master_doc = "index"

project = u"VHDL Numerical User Guides"
copyright = u"2022, Unai Martinez-Corral and contributors"
author = u"Unai Martinez-Corral and contributors"

version = "latest"
release = version  # The full version, including alpha/beta/rc tags.

language = None

exclude_patterns = []

# reST settings
prologPath = "prolog.inc"
try:
    with open(prologPath, "r") as prologFile:
        rst_prolog = prologFile.read()
except Exception as ex:
    print("[ERROR:] While reading '{0!s}'.".format(prologPath))
    print(ex)
    rst_prolog = ""

numfig = True

# -- Options for HTML output ----------------------------------------------

html_context = {}
ctx = ROOT / "context.json"
if ctx.is_file():
    html_context.update(loads(ctx.open("r").read()))

if (ROOT / "_theme").is_dir():
    html_theme_path = ["."]
    html_theme = "_theme"
    html_theme_options = {
        'logo_only': True,
        'home_breadcrumbs': False,
        'vcs_pageview_mode': 'blob',
    }
else:
    html_theme = "alabaster"

html_static_path = ["_static"]

#html_logo = str(Path(html_static_path[0]) / "logo" / "logo.svg")
#html_favicon = str(Path(html_static_path[0]) / "logo" / "icon.ico")

htmlhelp_basename = "VHDLNumDoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    "papersize": "a4paper",
}

latex_documents = [
    (master_doc, "VHDLNumDoc.tex", u"VHDL Numerical User Guides", author, "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "VHDLNum", u"VHDL Numerical User Guides", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (
        master_doc,
        "VHDLNum",
        u"VHDL Numerical User Guides",
        author,
        "VHDL",
        "HDL verification.",
        "Miscellaneous",
    ),
]

# -- Sphinx.Ext.InterSphinx -----------------------------------------------

intersphinx_mapping = {
    "python":     ("https://docs.python.org/3/", None),
    "edaa":       ("https://edaa-org.github.io/", None),
    "ghdl":       ("https://ghdl.github.io/ghdl", None),
    "ghdl-cosim": ("https://ghdl.github.io/ghdl-cosim", None),
    "vhdlmodel":  ("https://vhdl.github.io/pyVHDLModel", None),
    "vunit":      ("https://vunit.github.io", None),
    "cocotb":     ("https://docs.cocotb.org/en/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
}

# -- Sphinx.Ext.ExtLinks --------------------------------------------------
extlinks = {
    "wikipedia": ("https://en.wikipedia.org/wiki/%s", "wikipedia:"),
    "web": ("https://%s", ""),
    "bbrepo": ("https://bitbucket.org/%s", "bb:"),
    "glrepo": ("https://gitlab.com/%s", "gl:"),
    "ghrepo": ("https://github.com/%s", "gh:"),
    "ghsharp": ("https://github.com/umarcor/VHDLNumericUserGuides/issues/%s", "#"),
    "ghissue": ("https://github.com/umarcor/VHDLNumericUserGuides/issues/%s", "issue #"),
    "ghpull": ("https://github.com/umarcor/VHDLNumericUserGuides/pull/%s", "pull request #"),
    "ghsrc": ("https://github.com/umarcor/VHDLNumericUserGuides/blob/main/%s", ""),
    "gdocs": ("https://docs.google.com/document/d/%s", None),
    "gdraws": ("https://docs.google.com/drawings/d/%s", None),
    "pypi": ("https://pypi.org/project/%s", "pypi:"),
    "gitter": ("https://gitter.im/%s", "gitter:"),
    "youtube": ("https://www.youtube.com/watch?%s", "youtube:")
}
