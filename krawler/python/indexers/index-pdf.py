import urllib2 
from bs4 import BeautifulSoup
import os, os.path
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index

schema = Schema(content = TEXT(stored=False, phrase=True, analyzer=StemmingAnalyzer()),
                url = ID(stored=True))

if not os.path.exists("pdf-indexdir"):
    os.mkdir("pdf-indexdir")

ix = index.create_in("pdf-indexdir", schema)
writer = ix.writer()

file = open("non-html.txt","r")
pdf_list = file.readlines()
count = 0

for link in pdf_list:

    if link.endswith(".pdf\n") is True:

        try:
            #download pdf
            response = urllib2.urlopen(link)
            file = open("document.pdf","wb")
            file.write(response.read())
            file.close()
            
            #Open file to read into pdfobject and then delete pdf file
            pdf = "document.pdf"
            output = "document.txt"
            os.system("pdftotext "+pdf+" "+output)
            file = open("document.txt", "r")
            Content = file.read()
            file.close()

            #delete temp files
            os.remove(pdf)
            os.remove(output)

        except:
            print "failed"
            continue

        #convert to unicode
        if Content == "":
            Content = u"dump"
        Content = unicode(Content, "utf-8")
        link = unicode(link, "utf-8")
        
        writer.add_document(content=Content, url=link)

        count += 1
        print count

    else:
        continue

writer.commit()