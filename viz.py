import nltk
from nltk.tokenize import *
from nltk.corpus import stopwords
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd
import glob

# make a directory to put the files inside it
path_csv = '/Users/Mahmud/Desktop/nltk_output/csv' 
try: 
    os.makedirs(path_csv)
except OSError:
    if not os.path.isdir(path_csv):
        raise

path_graph = '/Users/Mahmud/Desktop/nltk_output/graphs' 
try: 
    os.makedirs(path_graph)
except OSError:
    if not os.path.isdir(path_graph):
        raise

transcripts = os.listdir('/Users/Mahmud/Desktop/PROJECT/files')  
index_begin = 1
index_end = 2

number = 1
path_file = '/Users/Mahmud/Desktop/PROJECT/files' 
for infile in glob.glob(os.path.join(path_file, '*.txt')):
  with open(infile, 'r') as myfile:
    data = myfile.read()
# separate the transcript by sentence
# can also separate it by word, using word_tokenize
# first index is the garbage, that needs to be cleaned
  words = word_tokenize(data)

  # we can use stop words to filter out common useless words that
  # are not important for text analysis

  stop_words = set(stopwords.words('English'))
  # this code appends to the stopword list: 
  stop_words.update((',', '.', '>', '<', ':', '--', '- -'))

  # create an empty list to which we'll add the relevant words that
  # are not in the stop_words set
  filtered = []

  for word in words:
  	if word not in stop_words:
  		filtered.append(word)

  n = 15

  csv_file = csv.writer(open('/Users/Mahmud/Desktop/nltk_output/csv/text'+str(number)+'.csv', 'w'))

  allWordDist = nltk.FreqDist(w.lower() for w in filtered)
  mostCommon= allWordDist.most_common(n)

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
  df = pd.DataFrame(dafr)
  # fdist.plot(n, cumulative=False, title="Frequency")

  df.to_csv('/Users/Mahmud/Desktop/nltk_output/csv/text'+str(number)+'.csv')

  df = pd.read_csv('/Users/Mahmud/Desktop/nltk_output/csv/text' +str(number)+'.csv', index_col=0)
  
  # consider figsize parameter
  ax = df[['words','freq']].plot(kind='bar', x='words', y='freq', figsize=(16,12), title ="15 Most Common Words", legend=True, fontsize=10)
  plt.savefig('/Users/Mahmud/Desktop/nltk_output/graphs/test'+str(number)+'.png')

  old_file = '/Users/Mahmud/Desktop/nltk_output/graphs/test' + str(number) + '.png'
  new_file = '/Users/Mahmud/Desktop/nltk_output/graphs/' + str(transcripts[index_begin:index_end]) + '.png'
  os.rename(old_file, new_file)
  print('renamed PNG' + str(number))

  old_file_csv = '/Users/Mahmud/Desktop/nltk_output/csv/text' + str(number) + '.csv'
  new_file_csv = '/Users/Mahmud/Desktop/nltk_output/csv/' + str(transcripts[index_begin:index_end]) + '.csv'
  os.rename(old_file_csv, new_file_csv)
  print('renamed CSV' + str(number))

  number += 1
  index_begin += 1
  index_end += 1
