# ImageMagick

https://legacy.imagemagick.org/

beaucoup d'exemple ici > https://legacy.imagemagick.org/Usage/

## Programme cross platforms pour modifier les images 

### commandes de bases (debian ?)

- convertir une image du jpg au png

`convert image.jpg image.png`

- rotation 90° horaire ?

`convert image.jpg -rotate 90 image-rotated.jpg`

- réduire à 200px

`convert image.jpg -resize 200 image-rotated.jpg`

- modifier la luminosité et le contraste

`convert image.jpg -brightness-contrast 10x15 image-rotated.jpg`