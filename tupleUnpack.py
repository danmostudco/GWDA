#raw_text = open("news_article.txt").read()
raw_text = open("news_article.txt").read()

conversionData = [(u'John Boehner', u'PERSON'), (u'Keystone Pipeline', u'ORGANIZATION'), (u'Obama', u'PERSON'), (u'Republican House', u'ORGANIZATION'), (u'John Boehner', u'PERSON'), (u'Keystone Pipeline', u'ORGANIZATION'), (u'Keystone Pipeline', u'ORGANIZATION'), (u'Boehner', u'PERSON'), (u'America', u'LOCATION'), (u'United States', u'LOCATION'), (u'Keystone Pipeline', u'ORGANIZATION'), (u'Keystone Pipeline', u'ORGANIZATION'), (u'Boehner', u'PERSON'), (u'State Department', u'ORGANIZATION'), (u'GOP', u'ORGANIZATION'), (u'Obama', u'PERSON')]

for pair in conversionData:
    findPhrase = pair[0]
    replacePhrase = pair[1]

    raw_text.replace(findPhrase, replacePhrase)
    raw_text = raw_text.replace(findPhrase, replacePhrase)

print raw_text


