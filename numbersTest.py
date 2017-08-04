import re

testData = """
there are 3 guys outside
703-509-0881,
67498738293,
713.853.5984,
713.646.8381 (fax)
EMAIL_ADDRESS"""

# def numberScrubber(text):
#     listofNumbers = []
#     match = re.findall(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?", text)    
#     for hit in match:
#         print(hit)
#         listofNumbers.append(hit)
    
#     for row in listofNumbers:
#         findPhrase = row
#         replacePhrase = "XXX-XXX-XXXX"
#         text = text.replace(findPhrase, replacePhrase)

#     #return the final phone text output
#     print("done")
#     return(text)

def numberScrubber(text):
    freshText = re.sub("\d+", "###", text)
    print freshText

numberScrubber(testData)