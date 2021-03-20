from util import *

import nltk
nltk.download('stopwords')

# Add your import statements here

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		for i in range(len(text)):
			final_tokens = []
			tokens = text[i]
			for W in tokens:
				if W not in stop_words:
					final_tokens.append(W)
			text[i] = final_tokens
			# Replace the corresponding tokenized sentence with final_tokens
		
		return text




	
