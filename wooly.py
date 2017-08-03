# -*- coding: utf-8 -*-
# make sure you set up stanford-ner folder and include the .gz and .jar files
import nltk
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')
text = """
In 2013, Peter Hollens was an aspiring a cappella singer surviving, in his words, by living on ramen in someone else’s house. Hollens was hardly new to the music business; he’d been a record producer and cruise singer before striking out on his own, and his wife Evynne co-founded the college a cappella group that inspired Pitch Perfect. His elaborate, multi-layered covers of pop songs had won him a dedicated following, but none of that translated to financial success. He was unsigned, song sales on platforms like iTunes were unpredictable, YouTube advertising revenue was “minuscule,” and since he covered other artists’ work, sponsor deals were legally complicated. """


for sent in nltk.sent_tokenize(text):
    tokens = nltk.tokenize.word_tokenize(sent)
    tags = st.tag(tokens)
    for tag in tags:
        if tag[1]=='PERSON': print tag


print("done")