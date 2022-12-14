#!/bin/bash

# réduire de 50% toutes les images .jpg dans le dossier courant
for f in *.jpg; do
    convert ${f} -resize 50% "${f%}.jpg"
done