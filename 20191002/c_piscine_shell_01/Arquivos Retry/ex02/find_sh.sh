#!/bin/sh
find . -type f -name '*.sh' -print | sed 's/\.sh//' | rev | cut -d '/' -f1 | rev
