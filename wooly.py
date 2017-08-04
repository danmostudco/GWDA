import nltk
import numpy as np
import re
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree

originText = open("test_Emails.txt").read()

# Process Text
def process_text(text):
	token_text = word_tokenize(text)
	return token_text

# NLTK POS and NER taggers   
def nltk_tagger(token_text):
	tagged_words = nltk.pos_tag(token_text)
	ne_tagged = nltk.ne_chunk(tagged_words)
	return(ne_tagged)

# Tag tokens with standard NLP BIO tags
def bio_tagger(ne_tagged):
		bio_tagged = []
		prev_tag = "O"
		for token, tag in ne_tagged:
			if tag == "O": #O
				bio_tagged.append((token, tag))
				prev_tag = tag
				continue
			if tag != "O" and prev_tag == "O": # Begin NE
				bio_tagged.append((token, "B-"+tag))
				prev_tag = tag
			elif prev_tag != "O" and prev_tag == tag: # Inside NE
				bio_tagged.append((token, "I-"+tag))
				prev_tag = tag
			elif prev_tag != "O" and prev_tag != tag: # Adjacent NE
				bio_tagged.append((token, "B-"+tag))
				prev_tag = tag
		return bio_tagged

# Parse named entities from tree
def structure_ne(ne_tree):
	ne = []
	for subtree in ne_tree:
		if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
			ne_label = subtree.label()
			ne_string = " ".join([token for token, pos in subtree.leaves()])
			ne.append((ne_string, ne_label))
	return ne

def nltkAnonymizer(text):
    nltkText = text

    # generate list of tuples with Detected Entity in index 0 and entity type in index 1
    conversionList = structure_ne(nltk_tagger(process_text(nltkText)))

    #for each pair, find and replace in the passed text
    for pair in conversionList:
        findPhrase = pair[0]
        replacePhrase = pair[1]
        nltkText = nltkText.replace(findPhrase, replacePhrase)

    # return the final text output
    return nltkText

#remove any email addresses
def emailScrubber(text):
    listOfEmails = []
    #EMAIL_REGEX = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
    match = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    for hit in match:
        listOfEmails.append(hit)

    for row in listOfEmails:
        findPhrase = row
        replacePhrase = "EMAIL_ADDRESS"
        text = text.replace(findPhrase, replacePhrase)
    
    # return the final email text output
    return text

def numberNuker(text):
    newText = re.sub("\d+", "###", text)
    return newText


# the grand finale, the beast arrives
def woolyAnonymizer(text):
    nltkText = nltkAnonymizer(text)
    emailText = emailScrubber(nltkText)
    numberText = numberNuker(emailText)

    # print the final output
    print numberText
    return numberText

# call the final wooly anonymizer function
woolyAnonymizer(originText)
