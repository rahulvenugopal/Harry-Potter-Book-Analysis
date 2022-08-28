# The script is to visualise total word count per chapter for every HP book
# Many thanks to Cedric Scherer for his tidy tuesday viz
# This plot is inspired and code help is from his IMDB dataviz
# https://github.com/Z3tt/TidyTuesday/blob/master/R/2020_12_TheOffice.Rmd
# author @ Rahul Venugopal

# Loading packages
library(tidyverse)
library(cowplot)
library(showtext)
library(png)
library(ggblur)

## ggplot theme
theme_set(theme_minimal(base_family = "Roboto Mono"))

theme_update(plot.background = element_rect(fill = "#fafaf5", color = "#fafaf5"),
             panel.background = element_rect(fill = NA, color = NA),
             panel.border = element_rect(fill = NA, color = NA),
             panel.grid.major.x = element_blank(),
             panel.grid.minor = element_blank(),
             axis.text.x = element_blank(),
             axis.text.y = element_text(size = 10),
             axis.ticks = element_blank(),
             axis.title.y = element_text(size = 13, 
                                         margin = margin(r = 10)),
             legend.position = "none",
             # legend.title = element_text(size = 9),
             plot.caption = element_text(family = "Special Elite",
                                         size = 10,
                                         color = "#393130",
                                         face = "bold",
                                         hjust = .5,
                                         margin = margin(5, 0, 20, 0)),
             plot.margin = margin(10, 25, 10, 25))

# hex to RGB and color viewer
# https://www.rapidtables.com/convert/color/hex-to-rgb.html

df_harry <- readr::read_csv('data/Harry-Potter-Chapter-Lengths.csv')

df_harry_avg <-
  df_harry %>% 
  arrange(Book, Chapter) %>% 
  mutate(Chapter_id = row_number()) %>% 
  group_by(Book) %>% 
  mutate(
    avg = mean(Word_count),
    Chapter_mod = Chapter_id + (7 * Book),
    mid = mean(Chapter_mod)
  ) %>% 
  ungroup() %>% 
  mutate(Book = factor(Book))
df_lines <-
  df_harry_avg %>% 
  group_by(Book) %>% 
  summarize(
    start_x = min(Chapter_mod) - 5,
    end_x = max(Chapter_mod) + 5,
    y = unique(avg)
  ) %>% 
  pivot_longer(
    cols = c(start_x, end_x),
    names_to = "type",
    values_to = "x"
  ) %>% 
  mutate(
    x_group = if_else(type == "start_x", x + .1, x - .1),
    x_group = if_else(type == "start_x" & x == min(x), x_group - .1, x_group),
    x_group = if_else(type == "end_x" & x == max(x), x_group + .1, x_group)
  )


# ggplot
p <- df_harry_avg %>% 
  
  # x and y axis
  ggplot(aes(Chapter_mod, Word_count)) +
  
  # Drawing horizontal lines
  geom_hline(data = tibble(y = seq(1500,9500,1000)),
             aes(yintercept = y),
             color = "grey82",
             size = .5) +
  
  # Drawing segments
  geom_segment(aes(xend = Chapter_mod,
                   yend = avg, 
                   color = Book, 
                   color = after_scale(colorspace::lighten(color, .2)))) +

  geom_line(data = df_lines,
            aes(x_group, y, 
                color = Book, 
                color = after_scale(colorspace::darken(color, .2))),
            size = 2.5) +
  
  geom_point_blur(aes(color = Book, shape = Book), blur_size = 0.5) +
  scale_shape_manual(values=c(16,16,16,16,16,16,16)) + 

  
# geom_point shapes
# http://sape.inf.usi.ch/quick-reference/ggplot2/shape  
  
  geom_label(aes(mid, 9300.9500,
                 label = glue::glue(" HP {Book} "),
                 color = Book, 
                 color = after_scale(colorspace::darken(color, .2))),
             fill = NA,
             family = "Special Elite",
             fontface = "bold",
             label.padding = unit(.2, "lines"), # amount of padding
             label.r = unit(.25, "lines"), # radius of rounder corner
             label.size = 0.5) + # size of the border
  
  scale_x_continuous(expand = c(.015, .015)) +
  
  scale_y_continuous(expand = c(.05, .05),
                     limits = c(1000,9500),
                     breaks = seq(1000,9500, by = 1000),
                     sec.axis = dup_axis(name = NULL)) +
  
  # Will add Harry Potter theme based color palette
  
  # scale_color_manual(values = c("#486090", "#D7BFA6", "#6078A8", "#9CCCCC", 
  #                               "#7890A8", "#C7B0C1", "#B5C9C9"),
  #                    guide = F) +

  labs(x = NULL,
       y = "Total words count",
       caption = "Visualization by Rahul Venugopal  •  Harrypotter verse")

logo <- readPNG('images/hp_logo.png')

ggdraw(p) +
  draw_image(logo, x = -.375, y = -.34, scale = 0.25)

ggsave(here::here("HowBigisHP.pdf"), 
       width = 18, height = 9, device = cairo_pdf)

# Note embedding fonts
# Locate ghostscript .exe
# Sys.setenv(R_GSCMD = "C:/Program Files (x86)/gs/gs9.02/bin/gswin32.exe")
# embed_fonts("newfont.pdf")
# cairo initializes a new graphics device that uses the cairo graphics library for rendering.
# The current implementation produces high-quality PNG, JPEG, TIFF bitmap files,
# high resolution PDF files with embedded fonts, SVG graphics and PostScript files.

# It also provides X11 and Windows interactive graphics devices
# Unlike other devices it supports all graphics features including alpha blending,
# anti-aliasing etc