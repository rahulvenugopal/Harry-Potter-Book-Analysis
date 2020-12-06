library(tidyverse)
library(ggtextures)
library(magick)
#> Linking to ImageMagick 6.9.9.39
#> Enabled features: cairo, fontconfig, freetype, lcms, pango, rsvg, webp
#> Disabled features: fftw, ghostscript, x11

data <- tibble(
  count = c(5, 6, 6, 4, 2, 3),
  animal = c("giraffe", "elephant", "horse", "bird", "turtle", "dog"),
  image = list(
    image_read_svg("http://steveharoz.com/research/isotype/icons/giraffe.svg"),
    image_read_svg("http://steveharoz.com/research/isotype/icons/elephant.svg"),
    image_read_svg("http://steveharoz.com/research/isotype/icons/horse.svg"),
    image_read_svg("http://steveharoz.com/research/isotype/icons/bird.svg"),
    image_read_svg("http://steveharoz.com/research/isotype/icons/turtle.svg"),
    image_read_svg("http://steveharoz.com/research/isotype/icons/dog.svg")
  )
)

ggplot(data, aes(animal, count, fill = animal, image = image)) +
  geom_isotype_col(
    img_height = grid::unit(1, "null"), img_width = NULL,
    ncol = 1, nrow = 1, hjust = 0.99, vjust = 1
  ) +
  coord_flip() +
  guides(fill = "none") +
  theme_minimal()