import nltk
import numpy as np
import re
from nltk import pos_tag
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree

originText = open("test_Article.txt").read()

# Process Text
def process_text():
	raw_text = originText
	token_text = word_tokenize(raw_text)
	return token_text

# Define the NER Tagger from Stanford
def stanford_tagger(token_text):
    st = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')
    ne_tagged = st.tag(token_text)
    return ne_tagged

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

# Create tree       
def stanford_tree(bio_tagged):
	tokens, ne_tags = zip(*bio_tagged)
	pos_tags = [pos for token, pos in pos_tag(tokens)]

	conlltags = [(token, pos, ne) for token, pos, ne in zip(tokens, pos_tags, ne_tags)]
	ne_tree = conlltags2tree(conlltags)
	return ne_tree

# Parse named entities from tree
def structure_ne(ne_tree):
	ne = []
	for subtree in ne_tree:
		if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
			ne_label = subtree.label()
			ne_string = " ".join([token for token, pos in subtree.leaves()])
			ne.append((ne_string, ne_label))
	return ne

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

def stanfordAnonymizer(text):
    stanfordText = text
    
    # generate list of tuples with Detected Entity in index 0 and entity type in index 1
    conversionList = structure_ne(stanford_tree(bio_tagger(stanford_tagger(process_text()))))

    # for each pair, find and replace in the passed text
    for pair in conversionList:
        findPhrase = pair[0]
        replacePhrase = pair[1]
        stanfordText = stanfordText.replace(findPhrase, replacePhrase)

    # return the final text output
    return stanfordText


def woolyAnonymizer(text):
    stanfordText = stanfordAnonymizer(text)
    emailText = emailScrubber(stanfordText)
    numberText = numberNuker(emailText)

    # print the final output
    return numberText

# call the final wooly anonymizer function
newText = woolyAnonymizer(originText)

finalPrint = woolyAnonymizer(newText)

print finalPrint
