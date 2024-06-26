# Harry Potter Book Analysis
JK Rowling wrote a series of 7 fantasy novels which took the world by storm :tornado:

~I just finished the fifth book and just started 6th book~ I completed reading all 7 books :books: and 8 movies :movie_camera:

This repo's goal is to learn some common useful NLP (Natural Language Processing) methods, graph theory concepts and cool visualisations

Another side goal is to document the code as close to [PEP 8](https://www.python.org/dev/peps/pep-0008/)

Doc string [PEP 257](https://www.python.org/dev/peps/pep-0257/)

---

## Word clouds

##### World cloud should reflect the name or central theme of each book

![Combined gif](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/images/hp_world.gif)

Philosopher's Stone (1997) | Chamber of Secrets (1998) | Prisoner of Azkaban (1999)

Goblet of Fire (2000) | Order of the Phoenix (2003) | Half-Blood Prince (2005) | Deathly Hallows (2007)

## Glossary of 7 books

##### Name of each book and cover image made of word cloud

![Cover](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/images/gridplot/HP_Grid.jpg)

## How big is Harry Potter verse

##### Number of chapters in each book and total words in each book

![CoverImage](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/images/HowBigisHP.png)

Code can be seen [here](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/code/harry_words.R) and PDF image [here](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/HowBigisHP.pdf)

Note : Add one small image theming each book, book name, update font to Lumos or HP font

Also do annotations, smallest chapter, largest chapter, smallest and largest book

## Spell analysis in HP series

This was motivated by the amazing [visualisation](https://public.tableau.com/en-us/gallery/spells-harry-potter) in Tableau by Skyler Johnson

Data was exported from Tableau and cleaned to tidy format

Yet to incorporate the interactive bits!

![CoverImagefromR](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/images/HP_spello.png)

- x-axis is location within the book (All books were merged as a single text)
- y-axis shows the spell and each dot is coloured coding the book in which it appears
- Failed to colour the y-axis text based on `Type` of spell (**Charm, Curse or Spell**)
  Have to figure out a way to assign axis text color based on a variable and circumvent the issue below
  ![Error](https://github.com/rahulvenugopal/Harry-Potter-Book-Analysis/blob/main/images/error.png)
- Learned ggplot objects in some detail. Thanks to [George Karamanis](https://github.com/gkaramanis) 
- Twitter folks suggested to hide y-axis text and use `ggtext` to control aes/color of y-axis text

##### Number of unique words in each book

##### Number of unique characters in each book

## Harry potter colour palette

Color palette which captures HP movies, four houses etc.
[harrypotter](https://github.com/aljrico/harrypotter) package in R and documentation [here](https://cran.r-project.org/web/packages/harrypotter/harrypotter.pdf)

## Trivia

1. There is a [course](https://uwaterloo.ca/scholar/fcondon/classes/popular-potter) offered by University of Waterloo called popular potter (engl 108p). Check out their [syllabus](https://uwaterloo.ca/scholar/sites/ca.scholar/files/fcondon/files/hp_pp_f2020_syllabus.pdf). I have never read a cool syllabus like this before!
2. ACCIO data is an infographic [book](https://www.blurb.com/books/8807266-accio-data) from Olivia Rouse. This 80 pages visual guide is a feast for any visual data story enthusiast

#### References

- [VisuProject_HarryPotterSpells](https://github.com/Graunarmin/VisuProject_HarryPotterSpells)
  - Output is an interactive html
  - Spells are ordered in appearance order. Size of bubble depends of number of times spell was used
    Connection via arcs
- [Harry-Potter-Viz](https://github.com/heatherjcohen/Harry-Potter-Viz)
  - Cool wordcloud viz
  - Colours are part of clouds which are themed with images
- [potter_spells](https://github.com/Vibhu-Agarwal/potter_spells)
  - A python package to list all HP spells
- [HP-text-mining](https://github.com/ErikaJacobs/Harry-Potter-Text-Mining)
  - Wordcloud in an image background
- [HarryPotter-Sentiment-Contribution](https://github.com/adityaab14/HarryPotter-Sentiment-Contribution)
  - Sentiment analysis using R
- Spell the spells in [Tableau](https://public.tableau.com/pt-br/gallery/harry-potter-spells-complete-list?tab=featured&type=featured)