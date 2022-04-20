#!/usr/bin/env python

# Python Standard Library
import os
from pathlib import Path
from typing import Optional

# First-Party Librairies
import pandoc

# Third-Party Librairies
from plumbum import FG
from plumbum.cmd import python
import typer

options = [
    "--standalone",
    "--toc",
    "--toc-depth=2",
    "--mathjax",
    "--css=css/style.css",
    "--include-in-header=html/font.html",
    "--variable=lang:en",
    # Bibliography
    "--bibliography=bibliography.json",
    "--citeproc",
    "--metadata=link-citations:true",
]


def generate_videos():
    cwd = Path.cwd()
    try:
        os.chdir(cwd / "python")
        python["vinograd.py"] & FG
    finally:
        os.chdir(cwd)


def generate_html():
    doc = pandoc.read(file="index.md")
    pandoc.write(doc, file="index.html", options=options)


def main(
    all: bool = typer.Option(False, help="Generate all assets."),
):
    if all:
        generate_videos()
    generate_html()


if __name__ == "__main__":
    typer.run(main)
