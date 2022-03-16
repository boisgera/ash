#!/usr/bin/env bash

pandoc --standalone \
  --metadata pagetitle="Asymptotic Stability for Humans" \
  --css css/style.css \
  --include-in-header html/font.html \
  -V lang=en \
  -f gfm \
  -o doc.html doc.md
