
"""
Created on Sun Nov 15 19:31:31 2020.

Data - Harry potter book series in .txt format

Section 1 - Wordcloud
Creating a word cloud in the shape of general theme of the book
texts in harry potter font

Giving credits where its due
Motivation + Source - https://github.com/heatherjcohen/Harry-Potter-Viz
@author: Rahul Venugopal
"""

#%% Loading libraries

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import requests
from bs4 import BeautifulSoup
import re
from io import BytesIO
import datetime
import random

# Custom functions for colour
# HSL (Hue, Saturation, Lightness)
# Hue is a degree on colour wheel with range 0 to 360
# 0 is red | 120 is green | 240 is blue
# Saturation (purity) is a percentage value 0 means gray, 100 means full colour
# Lightness is also percentage value, 0 is black 100 is white
# Read this https://sujansundareswaran.com/blog/why-hsl-is-better-than-hex-and-rgb

# https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html

def green_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    """
    Set the color theme of the cloud by recolor and custom coloring functions.

    Parameters
    ----------
    word : TYPE
        DESCRIPTION.
    font_size : TYPE
        DESCRIPTION. Integer
    position : TYPE
        DESCRIPTION. (x, y) coordinates
    orientation : TYPE
        DESCRIPTION. Eg Image.ROTATE_90
    random_state : TYPE, optional
        DESCRIPTION. The default is None. If a random object is given, this is
        is used for generating random numbers
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return "hsl(%d, %d%%, %d%%)" % (random.randint(87, 154), random.randint(0, 100) ,random.randint(0, 100))


def random_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(0, 350), random.randint(0, 100) ,random.randint(0, 100))


def red_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(0, 6), random.randint(0, 100) ,random.randint(0, 100))


def orange_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(14, 38), random.randint(0, 100) ,random.randint(0, 100))


def yellow_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(39, 69), random.randint(0, 100) ,random.randint(0, 100))


def teal_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(147, 180), random.randint(0, 100) ,random.randint(0, 100))


def lightblue_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(180, 200), random.randint(0, 100) ,random.randint(0, 100))


def darkblue_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(208, 250), random.randint(0, 100) ,random.randint(0, 100))


def purple_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(256, 283), random.randint(0, 100) ,random.randint(0, 100))


def pink_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(293, 341), random.randint(0, 100) ,random.randint(0, 100))

# Extra check to prevent below words falling to cloud
# There ought to be a better way using regex??
def remove_tuples(df):
    df=df.replace('said Harry', '')
    df=df.replace('said Ron', '')
    df=df.replace('said Hermione', '')
    df=df.replace('he said', '')
    df=df.replace('Ron and', '')
    df=df.replace('Harry and', '')
    df=df.replace('Hermione and', '')
    df=df.replace('hi', '')
    df=df.replace('Harry had', '')
    df=df.replace('said', '')
    df=df.replace('He was', '')
    df=df.replace('It was', '')
    df=df.replace('still', '')
    df=df.replace('now', '')
    df=df.replace('though', '')
    df=df.replace('well', '')
    df=df.replace('and Harry', '')
    df=df.replace('wa', '')
    df=df.replace('Page     Harry Potter and the Philosophers Stone   J K  Rowling', '')
    return df

# Custom function to get full text from a url
def getcorpus(url):
    response = requests.get(url) #we get a raw html file
    soup = BeautifulSoup(response.text, "html.parser")
    words = soup.get_text()
    # Using regex to remove anything other than alphabets and space
    # ^ will complement the set
    # - is used to select range of characters
    words= re.sub("[^a-zA-Z' ]+"," ", words)
    return words

# cloud generation

# advanced cloud either local or url image
# special Harryp_ font downloaded from https://www.fontspace.com/category/harry-potter

def cloudify(text, imgloc, imgurl,maxsize ,
               maxwords, save, title, color, font,
              figsize):
    """
    Customise whole word cloud.

    Parameters
    ----------
    text : TYPE
        DESCRIPTION.
    imgloc : TYPE
        DESCRIPTION.
    imgurl : TYPE
        DESCRIPTION.
    maxsize : TYPE
        DESCRIPTION.
    maxwords : TYPE
        DESCRIPTION.
    save : TYPE
        DESCRIPTION.
    title : TYPE
        DESCRIPTION.
    color : TYPE
        DESCRIPTION.
    font : TYPE
        DESCRIPTION.
    figsize : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if imgloc == "local":
        mask = np.array(Image.open(imgurl))
    else:
        response1 = requests.get(imgurl)
        img = Image.open(BytesIO(response1.content))
        mask = np.array(img)

    wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\\' +str(font)+'.ttf',
                          stopwords = stopwords,
                          background_color="white",
                          max_words=maxwords,
                          max_font_size=maxsize,
                          collocations='False', # added this parameter
                          mask=mask).generate(text)

    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[figsize,figsize])
    plt.title(title)
    if color =="random":
        plt.imshow(wordcloud.recolor(color_func=random_color_func), interpolation="bilinear")
    elif color =="green":
        plt.imshow(wordcloud.recolor(color_func=green_func), interpolation="bilinear")
    elif color =="red":
        plt.imshow(wordcloud.recolor(color_func=red_func), interpolation="bilinear")
    elif color =="orange":
        plt.imshow(wordcloud.recolor(color_func=orange_func), interpolation="bilinear")
    elif color =="yellow":
        plt.imshow(wordcloud.recolor(color_func=yellow_func), interpolation="bilinear")
    elif color == "teal":
        plt.imshow(wordcloud.recolor(color_func=teal_func), interpolation="bilinear")
    elif color == "lightblue":
        plt.imshow(wordcloud.recolor(color_func=lightblue_func), interpolation="bilinear")
    elif color =='darkblue':
        plt.imshow(wordcloud.recolor(color_func=darkblue_func), interpolation="bilinear")
    elif color == "purple":
        plt.imshow(wordcloud.recolor(color_func=purple_func), interpolation="bilinear")
    elif color =="pink":
        plt.imshow(wordcloud.recolor(color_func=pink_func), interpolation="bilinear")
    else:
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    if save == "yes":
        plt.savefig("viz"+str(datetime.datetime.now().second)+str(datetime.datetime.now().minute)+".png", format="png")

 #%% Let us plot now

# Get the data
HP1 = getcorpus("https://github.com/formcept/whiteboard/blob/master/nbviewer/notebooks/data/harrypotter/Book%201%20-%20The%20Philosopher's%20Stone.txt")
HP1 =remove_tuples(HP1)

HP2 = getcorpus("http://www.pauladaunt.com/books/Children's/Harry_Potter1-4-1/J.%20K.%20Rowling%20-%20Harry%20Potter%202%20-%20The%20Chamber%20Of%20Secrets.txt")
HP2 =remove_tuples(HP2)

HP3 = getcorpus("http://www.pauladaunt.com/books/Children's/Harry_Potter1-4/J.%20K.%20Rowling%20-%20Harry%20Potter%203%20-%20Prisoner%20of%20Azkaban.txt")
HP3 =remove_tuples(HP3)

HP4 = getcorpus("https://cdn.preterhuman.net/texts/literature/books_by_title/N%20-%20S/Rowlings%20Goblet%20of%20Fire.txt")
HP4 =remove_tuples(HP4)

HP5 = getcorpus("https://raw.githubusercontent.com/bobdeng/owlreader/master/ERead/assets/books/Harry%20Potter%20and%20the%20Order%20of%20the%20Phoenix.txt")
HP5 =remove_tuples(HP5)

HP6 = getcorpus("https://github.com/bobdeng/owlreader/blob/master/ERead/assets/books/Harry%20Potter%20and%20The%20Half-Blood%20Prince.txt")
HP6 =remove_tuples(HP6)

HP7 = getcorpus("https://raw.githubusercontent.com/bobdeng/owlreader/master/ERead/assets/books/Harry%20Potter%20and%20the%20Deathly%20Hallows%20.txt")
HP7=remove_tuples(HP7)

# Set stopwords now
stopwords = set(STOPWORDS)

# Usze is function to randomly check unwanted words in text
stopwords.add('s')
stopwords.add('y')
stopwords.add('m')

cloudify(text = HP1,
           imgloc = "local",
           imgurl = "owl1.jpg",
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "purple",
           font = "HarryPotter-ov4z",
           figsize = 15)

cloudify(text = HP2,
           imgloc = "local",
           imgurl = "anotherdobby2.jpg", #snake2, dobby2
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "darkblue",
           font = "HarryPotter-ov4z",
           figsize = 15)

cloudify(text = HP3,
           imgloc = "local",
           imgurl = "stag3.jpg",
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "lightblue",
           font = "HarryPotter-ov4z",
           figsize = 15)

cloudify(text = HP4,
           imgloc = "local",
           imgurl = "goblet4.jpg",
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "teal",
           font = "HarryPotter-ov4z",
           figsize = 15)

cloudify(text = HP5,
           imgloc = "local",
           imgurl = "fawkes5.jpg", #fawkes5
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "",
           font = "HarryPotter-ov4z",
           figsize = 15)

cloudify(text = HP6,
           imgloc = "local",
           imgurl = "cauldron6.jpg",
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "green",
           font = "HarryPotter-ov4z",
           figsize = 15)

cloudify(text = HP7,
           imgloc = "local",
           imgurl = "snitch7.jpg",
           maxsize = 120,
           maxwords = 7000,
           save = "yes",
           title = "",
           color = "", # Give no color. It will adapt image color
           font = "HarryPotter-ov4z",
           figsize = 15)

#%% Gridplot

# Loading libraries
import itertools
import cv2
import os

#User defined variables
name = "HP_Grid" + ".jpg"
margin = 20 #Margin between pictures in pixels
width = 4 # Width of the matrix (nb of images)
height = 2 # Height of the matrix (nb of images)
panels = width*height

# rename the files as hp{1..7}
filename_list =  ['hp1.png', 'hp2.png', 'hp3.png',
         'hp4.png', 'hp5.png', 'hp6.png', 'hp7.png' ]


imgs = [cv2.imread(os.getcwd()+"/"+file) for file in filename_list]

# Define the shape of the image to be replicated
# (all images should have the same shape)
img_h, img_w, img_c = imgs[0].shape

#Define the margins in x and y directions
m_x = margin
m_y = margin

#Size of the full size image
mat_x = img_w * width + m_x * (width - 1)
mat_y = img_h * height + m_y * (height - 1)

#Create a matrix of zeros of the right size and fill with 255 (so margins end up white)
imgmatrix = np.zeros((mat_y, mat_x, img_c),np.uint8)
imgmatrix.fill(255)

#Prepare an iterable with the right dimensions
positions = itertools.product(range(height), range(width))

for (y_i, x_i), img in zip(positions, imgs):
    x = x_i * (img_w + m_x)
    y = y_i * (img_h + m_y)
    imgmatrix[y:y+img_h, x:x+img_w, :] = img

resized = cv2.resize(imgmatrix, (mat_x,mat_y), interpolation = cv2.INTER_AREA)
compression_params = [cv2.IMWRITE_JPEG_QUALITY, 100]
cv2.imwrite(name, resized, compression_params)
