#!/usr/bin/env bash

pandoc --standalone \
  --css css/style.css \
  --include-in-header html/font.html \
  -V lang=en \
  -o doc.html doc.md

pandoc --standalone \
  -V lang=en \
  -o doc.pdf doc.md