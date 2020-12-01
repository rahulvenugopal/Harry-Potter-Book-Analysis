# Loading libraries
library(tidyverse)

# Load data in csv
# Data is exported from https://public.tableau.com/en-us/gallery/spells-harry-potter
data <-read.csv('spells_cleaned.csv')

# Converting relevant columns to factors
data[, 2:5] <- lapply(data[, 2:5], as.factor)

# Snapshot summary of data
str(data)

# Last column is a snippet of text featuring spell
# Have to use this when I do interactive plots

# Let the plotting begin

p2 <- ggplot(data, aes(Spell, Loc, color = Book)) + # Color codes book
  
  geom_point() +
  
  coord_flip() + # Flip the axes for better view
  
  geom_hline(yintercept = 90000, linetype = "dashed", color = "#003153", size = 0.5) +
  
  geom_hline(yintercept = 200000, linetype = "dashed", color = "#28643D", size = 0.5) +
  
  geom_hline(yintercept = 320000, linetype ="dashed", color = "#222F5B", size = 0.5) +
  
  geom_hline(yintercept = 550000, linetype = "dashed", color = "#9DDAF9", size = 0.5) +
  
  geom_hline(yintercept = 840000, linetype = "dashed", color = "#b22222", size = 0.5) +
  
  geom_hline(yintercept = 1040000, linetype = "dashed", color = "#32cd32", size = 0.5) +

# Preview of viz
labs(
  title = "Spells casted in Harry Potter books",
  subtitle = "Word location of each spell is plotted along x-axis", width = 125,
  caption = "Data : Tableau viz by Skyler Johnson | Graphic: Rahul Venugopal"
) +
  
  theme_minimal(base_family = "IBM Plex Sans") +

  theme(
    
    # Adding color to y axis text
    axis.text.y = element_text(color = '#660000'),
    
    legend.position = "bottom", # Pushing legend to bottom
    
    legend.box = "horizontal",
    
    # Putting a box around legend
    legend.box.background = element_rect(fill = "grey98", color = "#aab5c1", size = 0.6),
    
    legend.text = element_text(size = 8, family = "IBM Plex Serif"),
    
    legend.title = element_blank(),

    panel.grid.minor = element_blank(),
    
    axis.title = element_blank(),
    
    # Removing text on x-axis
    axis.text.x = element_blank(),
    
    # Removing vertical gridlines
    panel.grid.major.x = element_blank(),
    
    plot.title = element_text(face = "bold", size = 30),
    
    plot.subtitle = element_text(margin = margin(0, 0, 20, 0)),
    
    plot.caption = element_text(margin = margin(20, 0, 0, 0)),
    
    plot.margin = margin(20, 20, 20, 20)
  ) +
  
  guides(colour = guide_legend(nrow = 1)) # Legend comes neatly in single row

# Makes geom_points crisper and kill alias effects by using type as cairo
ggsave("HP_spello.png", dpi = 300, width = 14, height = 15, type = 'cairo')