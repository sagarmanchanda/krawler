import os, os.path
from bs4 import BeautifulSoup
import urllib2
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index

schema = Schema(title = TEXT(stored=True, phrase=True, field_boost=100.0, analyzer=StemmingAnalyzer()),
                heading = TEXT(stored=False, phrase=True, field_boost=15.0, analyzer=StemmingAnalyzer()),
                content = TEXT(stored=False, phrase=True, analyzer=StemmingAnalyzer()),
                url = ID(stored=True))

if not os.path.exists("new-indexdir"):
    os.mkdir("new-indexdir")

ix = index.create_in("new-indexdir", schema)
writer = ix.writer()

file = open("updated-links.txt","r")
links_list = file.readlines()
count = 0
for link in links_list:

    try:
        content = urllib2.urlopen(link).read()
        soup = BeautifulSoup(content)
        count += 1
        print count

    except:
        continue

    Title = ""
    temps = soup.find_all("title")
    for temp in temps:
        Title = Title + temp.text + " "
    if Title == "":
        Title = u"dump"

    Heading1 = ""
    temps = soup.find_all("h1")
    for temp in temps:
        Heading1 = Heading1 + temp.text + " "

    temps = soup.find_all("h2")
    for temp in temps:
        Heading1 = Heading1 + temp.text + " "
    if Heading1 == "":
        Heading1 = u"dump"

    Paragraphs = ""
    temps = soup.find_all("p")
    for temp in temps:
        Paragraphs = Paragraphs + temp.text + " "
    if Paragraphs == "":
        Paragraphs = u"dump"

    link = unicode(link, "utf-8")

    writer.add_document(title=Title, heading=Heading1, content=Paragraphs, url=link)

writer.commit()

