#!/bin/bash

rm *.aux
rm *.lof
rm *.log
rm *.lot
rm *.out
rm *.toc

BASE="${1%.*}"
pdflatex $BASE.tex
if [ $? -ne 0 ]; then
    echo "Compilation error. Check log."
    exit 1
fi
bibtex $BASE
pdflatex $BASE.tex
pdflatex $BASE.tex
exit 0
