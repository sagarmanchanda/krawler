import urllib2 
from bs4 import BeautifulSoup
import os, os.path
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index
import json

schema = Schema(title = TEXT(stored=True, phrase=True, analyzer=StemmingAnalyzer()),
                pdf_url = ID(stored=True),
                doc_url = ID(stored=True))

if not os.path.exists("form-indexdir"):
    os.mkdir("form-indexdir")

ix = index.create_in("form-indexdir", schema)
writer = ix.writer()

json_data = open("forms.json","r")
form_data = json.load(json_data)

for form in form_data:

    Title = form['title']
    if form['pdf-url'] == "":
        Pdf_url = u""
    else:
        Pdf_url = form['pdf-url']
    Doc_url = form['doc-url']

    writer.add_document(title=Title, pdf_url=Pdf_url, doc_url=Doc_url)

writer.commit()