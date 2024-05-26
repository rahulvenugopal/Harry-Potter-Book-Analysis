# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:52:33 2024
- Data story from Harry Potter books
- To showcase multiple visual elements using plotnine library
- This serves as a template to build awesome visual data stories

@author: Rahul Venugopal
"""
#%% Load libraries
import pandas as pd
from plotnine import (
    ggplot,
    aes,
    geom_segment,
    after_scale,
    theme_classic,
    element_blank,
    theme,
    element_text,
    theme_set
)


#%% Load data
'''
- It is important to know about the dataset beyond what is there in the data
- We highlight certain meta book chapter trivia onto the viz
- We have a simple three column data: Chapter wise word count of each harry potter book (Yeah, that's it')
'''
data = pd.read_csv('data/Harry-Potter-Chapter-Lengths.csv')

#%% Planning the dataviz and create subsets of data which are required

# Min and Max (Chapter numbers) per book
chapters_per_book = data.groupby('Book')['Chapter'].agg([min,max]).reset_index()
# I should know where to draw the segments (start and end along x-axis which are chapters)
chapters_per_book['endpoints'] = chapters_per_book['max'].cumsum()
chapters_per_book['startpoints'] = chapters_per_book['endpoints'] - chapters_per_book['max'] + 1

chapters_per_book['Word Counts'] =data.groupby('Book')['Word_count'].mean().reset_index()['Word_count']

#%% Part 1: x axis in chronology of the book and y axis, mean count of words in each book
# It would be nice to have a horizontal plate (whose spread indicate book chapters) and height the mean words in the book
# Pick the colour of the plate based on some visual element from the actual book cover

# Part 2: Set up the theme | Harry potter font | Larger y labels |
# Remove x axis text, title and ticks | Remove the legend | Remove the vertical lines close to the x and y axis base | Set the y axis limits in multiples of 1000 to 10k

ggplot()+ geom_segment(chapters_per_book,
             aes(x = "startpoints",
                 xend = "endpoints",
                 y = "Word Counts",
                 yend = "Word Counts",
                 color = "Book",
                 fill = after_scale('color'), size=0.5))+ theme_classic() + theme(axis_title_x = element_blank(),
axis_text_x = element_blank(),
axis_ticks_x = element_blank(),
axis_title_y = element_text(size = 24),
axis_text_y = element_text(size = 12),
axis_line = element_blank(),
legend_position = "none",
text = element_text(family="Harry P"),
dpi = 600)
