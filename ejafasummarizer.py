
import io
import os
os.system('pip install nltk')
os.system('pip install sklearn')

import nltk

nltk.download('stopwords')
nltk.download('punkt')

filename = input("name of file to summerize: ")
f = open(filename,"r+")
text = f.read()


# convert to lower case
text = text.lower()


# seperate sentences
from nltk import sent_tokenize
sentences = sent_tokenize(text)


# remove punctuation from each line
import string
sentences = [line.translate(str.maketrans('', '', string.punctuation)) for line in sentences]


# split into words
from nltk.tokenize import word_tokenize
t_doc = [word_tokenize(line) for line in sentences]


# filter out stop words
# and stemming using PorterStemmer

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stop_words = set(stopwords.words('english'))
porter = PorterStemmer()

for line in t_doc:
  for word in line:
    if word in stop_words:
      t_doc[t_doc.index(line)].remove(word)
    else: # using PorterStemer
      t_doc[t_doc.index(line)][line.index(word)] = porter.stem(word)


# tf-idf using sklearn
# creating stemmed sentences

t_doc_s = list()
for line in t_doc:
  t_doc_s.append(" ".join(line[:]))
# print(t_doc_s)
# Calculating tf-idf and creating document matrix

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
vector = vectorizer.fit_transform(t_doc_s)



# k-means cluster
from sklearn.cluster import KMeans
import numpy as np

# asking for how many lines we need to summarize

n = int(input("how many output lines do you want for summarize: "))
kmeans = KMeans(n_clusters=n,max_iter=10000,n_init=1000).fit(vector)          
kmeans.cluster_centers_.shape

# calculating cosine similarity

from sklearn.metrics.pairwise import cosine_similarity
values = cosine_similarity(kmeans.cluster_centers_,vector)



# finding the nearest sentence for each cluster center with cosine similarity
line_no = list()
for i in values:
  line_no.append(list(i).index(i.max()))

# sorting to keep the flow of meaning 

line_no.sort() 
from nltk import sent_tokenize
s_sentences = sent_tokenize(text)
print("\nSummary: ")
for i in line_no:
  print(s_sentences[i])

input()