# The Great Wooly Data Anonymizer
A beast of burden tasked with masking the whereabouts of all who have walked before it.

## Purpose of the Anonymizer
When you are dealing with sensitive population data, it's best to scrub out common names, locations, organizations, and other named resources. This data anonymizer parses text passed into its tusks and goes about obfuscating any sensitive information. For this reason, any user can understand the context and situation in which the strings were written without compromising the identify of the users.

## Getting Started
Setup may depend on your machine. I recommend using a virtual environmnet and using pip to install packages within the virtual environment.

1. Install nltk and numpy through pip
2. Use the woolyAnonymizer() function to anonymize text

## Inspiration and Resources
[Chuck Dishmon's guest post](https://pythonprogramming.net/using-bio-tags-create-named-entity-lists/) on Stanford NER Taggers helped formulate much of the structure of early versions of this prototype.