'''
Identifying characters from a novel
Counting their total occurences
Visualising

Author @ Rahul Venugopal
'''
#%% Loading libraries
import nltk
from nltk import pos_tag, word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

from tqdm import tqdm
import re
import string
from itertools import combinations
from collections import Counter


from flair.models import SequenceTagger
from flair.data import Sentence

#%% Loading data
book = nltk.corpus.gutenberg.raw('carroll-alice.txt')
book

# Cleaning data
book = book.replace('\n', ' ')
book = book.replace('\r', ' ')
book = book.replace('\'', ' ')
book

sent = sent_tokenize(book)

# Use flair named entity recognition
tagger = SequenceTagger.load('ner')

# Get all the names of entities tagged as people

x = []

for line in tqdm(sent):
  sentence = Sentence(line)
  tagger.predict(sentence)
  for entity in sentence.to_dict(tag_type='ner')['entities']:
    if entity['type'] == 'PER':
      x.append(entity['text'])
      
      
# Remove any punctuation within the names
names = []
for name in x:
  names.append(name.translate(str.maketrans('', '', string.punctuation)))
  
# List characters by the frequency with which they are mentioned
result = [item for items, c in Counter(x).most_common() 
                                      for item in [items] * c] 

print(Counter(names).most_common())

common = [] 
main_freq = []
# Manually remove words that are not character names from our list

not_names = ['Well', 'Ive', 'Five', 'Theyre', 'Dont', 'Wow',  'Ill', 'Miss', 'Hush', 'Yes',]

for n,c in Counter(names).most_common():
  # if the character is mentioned less than 5 time, the name is not added to the main character list
  if c > 5 and n not in not_names:
    main_freq.append((n,c))
    common.append(n)
    
    
