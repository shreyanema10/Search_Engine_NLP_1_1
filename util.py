import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

def wordnet_form(pos):
    if pos.startswith("J"):
        return wordnet.ADJ
    elif pos.startswith("V"):
        return wordnet.VERB
    elif (pos.startswith("N")) | (pos.startswith("P")):
        return wordnet.NOUN
    elif pos.startswith("R"):
        return wordnet.ADV
    else:
        # else classify it as a noun
        return wordnet.NOUN



