from util import *

# Add your import statements here
import nltk
from nltk import sent_tokenize
nltk.download('punkt')
import re



class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""



		# endmarks in english ['.', '!', '?'] can be removed using re library
		segmentedText = re.split('\. |\?|\!|"', text)
		# remove empty sentences if any
		if '' in segmentedText:
			segmentedText.remove('')
			
		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		segmentedText = sent_tokenize(text)
		
		return segmentedText
