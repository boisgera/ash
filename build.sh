#!/usr/bin/env bash

pandoc \
  --standalone \
  --toc --toc-depth=2 \
  --mathjax \
  --css css/style.css \
  --include-in-header html/font.html \
  -V lang=en \
  -o doc.html doc.md
