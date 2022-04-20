#!/usr/bin/env python

# Python Standard Library
import os
from pathlib import Path
from typing import Optional

# First-Party Librairies
import pandoc

# Third-Party Librairies
from bs4 import BeautifulSoup; HTML = lambda arg: BeautifulSoup(arg, "html.parser")
from plumbum import FG
from plumbum.cmd import python
try:
    from plumbum.cmd import git
except ImportError:
    git = None
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
        os.chdir(cwd / "videos")
        python["main.py"] & FG
    finally:
        os.chdir(cwd)


def generate_html():
    doc = pandoc.read(file="index.md")
    pandoc.write(doc, file="index.html", options=options)

def post_process_html():
    with open("index.html", encoding="utf-8") as input:
        html = HTML(input)
    p = HTML("""
      <p>
        <span style='display:inline-block;width:1em;position:relative;margin-right:0.25em'>
          <img 
            style='position:relative;top:0.15em;'
            height='auto' width='100%' 
            src='icons/github.svg'>
          </img></span>
        <a 
          href='https://github.com/boisgera/ash'>
          https://github.com/boisgera/ash
        </a>
      </p>
    """)
    html.html.body.header.append(p)
    with open("index.html", "w", encoding="utf-8") as output:
        output.write(html.prettify())
    # if git:
    #     hash_ = git("rev-parse", "--short", "HEAD").strip()


def main(
    all: bool = typer.Option(False, help="Generate all assets."),
):
    if all:
        generate_videos()
    generate_html()
    post_process_html()



if __name__ == "__main__":
    typer.run(main)
