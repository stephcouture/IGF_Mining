import nltk
from nltk.tokenize import *
from nltk.corpus import stopwords
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd

# open a connection to the testing text file
with open('/Users/Mahmud/Desktop/text.txt', 'r') as myfile:
	data = myfile.read()

# make a directory to put the files inside it
path = '/Users/Mahmud/Desktop/nltk_output/csv' 
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise

path = '/Users/Mahmud/Desktop/nltk_output/graphs' 
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise

# separate the transcript by sentence
# can also separate it by word, using word_tokenize
# first index is the garbage, that needs to be cleaned
words = word_tokenize(data)

# we can use stop words to filter out common useless words that
# are not important for text analysis

stop_words = set(stopwords.words('English'))
# this code appends to the stopword list: 
stop_words.update((',', '.', 'i', '>', '<', ':', '--', '- -', 'I', 'Thank'))

# create an empty list to which we'll add the relevant words that
# are not in the stop_words set
filtered = []

for word in words:
	if word not in stop_words:
		filtered.append(word)

n = 20

csv_file = csv.writer(open('/Users/Mahmud/Desktop/nltk_output/csv/word_frequencies.csv', 'w'))

allWordDist = nltk.FreqDist(w.lower() for w in filtered)
mostCommon= allWordDist.most_common(n)
print(mostCommon)

fdist = nltk.FreqDist(filtered)

keys = []
counts = []
index = []
num = 0
for key, count in mostCommon:
   csv_file.writerow([key, count])
   keys.append(key)
   counts.append(count)
   index.append(num)
   num += 1

columns = [index, keys, counts]
names = ['index', 'words', 'freq']
dafr = dict(zip(names, columns))
print(dafr)
df = pd.DataFrame(dafr)
# fdist.plot(n, cumulative=False, title="Frequency")

df.to_csv('/Users/Mahmud/Desktop/nltk_output/csv/word_frequencies.csv')

df = pd.read_csv('/Users/Mahmud/Desktop/nltk_output/csv/word_frequencies.csv', index_col=0)
print(df)

# consider figsize parameter
ax = df[['words','freq']].plot(kind='bar', x='words', y='freq', title ="20 Most Common Words", legend=True, fontsize=12)
plt.savefig('/Users/Mahmud/Desktop/nltk_output/graphs/viz.png')
plt.show()


