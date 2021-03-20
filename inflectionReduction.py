from util import *

# Add your import statements here

import nltk
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		# as lemmatization gives better precision we used lemmatization
		lemmatizer = WordNetLemmatizer()
		for i in range(len(text)):
			# remove empty lists if any
			while '' in text[i]:
				text[i].remove('')
			postags = pos_tag(text[i])
			for wordnum in range(len(text[i])):
				# covert to wordnet understandable format (code in utility)
				POS = wordnet_form(postags[wordnum][1])
				# use lemmatizer to reduce tokens into their common base forms
				text[i][wordnum] = lemmatizer.lemmatize(text[i][wordnum], pos=POS)

		return text


