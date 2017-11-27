import nltk
print("Imported NLTK")

from nltk.tokenize import *
print("Imported NLTK Tokenizer")

from nltk.corpus import stopwords
print("Imported NLTK Stop Words")

from nltk.stem import PorterStemmer
print("Imported NLTK Porter Stemmer")

from nltk.tokenize import PunktSentenceTokenizer
print("Imported NLTK Punkt Tokenizer")

from nltk.corpus import state_union
print("Imported State Union Address to be Used as Train Set")

from nltk.stem import WordNetLemmatizer
print("Imported NLTK Lemmatizer")

# open a connection to the testing text file
with open('/Users/Mahmud/Desktop/text.txt', 'r') as myfile:
	data = myfile.read()

# separate the transcript by sentence
# can also separate it by word, using word_tokenize
# first index is the garbage, that needs to be cleaned
words = word_tokenize(data)

# we can use stop words to filter out common useless words that
# are not important for text analysis

stop_words = set(stopwords.words('English'))

# create an empty list to which we'll add the relevant words that
# are not in the stop_words set
filtered = []

for word in words:
	if word not in stop_words:
		filtered.append(word)
fob = open('/Users/Mahmud/Desktop/nltk_output/stop_words.txt', 'w')
fob.write(str(filtered))
fob.close()

# way of "normalisation" of a word, which gets rid of endings 
# of words and keeps the root. This is important because 
# two sentences may mean the same thing, so we want to get 
# rid of one of them
def stemming():
	ps = PorterStemmer()

	stemmed = []

	for word in filtered:
		root = ps.stem(word)
		stemmed.append(root)

	fob = open('/Users/Mahmud/Desktop/nltk_output/stemmed_words.txt', 'w')
	fob.write(str(stemmed))
	fob.close()

# speech tagging takes the text file and after having tokenized
# identifies words as nouns, verbs etc
def speech_tagger():
	train_text = state_union.raw('2005-GWBush.txt')

	custom_sent_token = PunktSentenceTokenizer(train_text)
	tokenized = custom_sent_token.tokenize(data)

	tagged_list = []
	for word in tokenized:
		ww = nltk.word_tokenize(word)
		tagged = nltk.pos_tag(ww)
		tagged_list.append(tagged)
	fob = open('/Users/Mahmud/Desktop/nltk_output/tagged_words.txt', 'w')
	fob.write(str(tagged_list))
	fob.close()

# chunking is grouping different words together using their speech tags, not 
# necessary for our purposes. Also we will skip chinking, which is part of chunking, 
# but it is the process of removing words from a chunked group

# lemmatizing is just like stemming, but the output will be a real word, or a synonym
def lemmatizee():
	lemmatizer = WordNetLemmatizer()

	lemma = []

	for word in words:
		lemmatized = lemmatizer.lemmatize(word)
		lemma.append(lemmatized)

	fob = open('/Users/Mahmud/Desktop/nltk_output/lemmatized.txt', 'w')
	fob.write(str(lemma))
	fob.close()

stop_wordz()
stemming()
speech_tagger()
lemmatizee()


