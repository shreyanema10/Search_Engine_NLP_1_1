from util import *
import nltk
from nltk.tokenize import TreebankWordTokenizer
import copy
import re



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""


		#Fill in code here
	
		tokenizedText = []
		for sent in text:
			# split the sentence at word separators like ' , -/ using re library
			tokenized_Text = re.split("[' ,-/]", sent)
			# copy tokenized list
			lst = copy.deepcopy(tokenized_Text)

			# remove unwanted words like punctuations, spaces and empty words
			for W in tokenized_Text:
				if W in ['?', ':', '!', '.', ',', ';', '"']:
					lst.remove(W)
				elif W =='':
					lst.remove(W)
				elif W == ' ':
					lst.remove(W)

				# append the list to super list
				tokenizedText.append(lst)

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		for sent in text:
			# tokenize sentence using tree bank algorithm
			tokens = TreebankWordTokenizer().tokenize(sent)
			for W in tokens:
				# in this case there won't be any empty words or spaces so just remove punctuations if any
				if W in ['?', ':', '!', '.', ',', ';']:
					tokens.remove(W)
					tokenizedText.append(tokens)



		return tokenizedText
