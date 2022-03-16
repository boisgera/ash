#!/usr/bin/env bash

pandoc --standalone \
  --mathjax \
  --css css/style.css \
  --include-in-header html/font.html \
  -V lang=en \
  -o doc.html doc.md
