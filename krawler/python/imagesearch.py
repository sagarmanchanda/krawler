#!/usr/bin/env python

from whoosh import index
from whoosh import qparser 
import urllib2
from bs4 import BeautifulSoup
import sys
import json

cmdargs = sys.argv

ix = index.open_dir("/opt/lampp/htdocs/web/python/indexdir")

searcher = ix.searcher()
result_dict = {}

serach_term = ""
dump = 0
for arg in cmdargs:
	if dump != 0:
		serach_term = serach_term + str(arg) + " "
	dump += 1

serach_term = unicode(serach_term, "utf-8")

qp = qparser.MultifieldParser(["title", "heading", "content"], ix.schema)
q = qp.parse(serach_term) 	
results = searcher.search(q,limit=20)


data = {}
data['images'] = []
data['didyoumean'] = ""

if len(results) == 0:
	corrected = searcher.correct_query(q, serach_term)
	if corrected.query != q:
	     data['didyoumean'] = corrected.string

for result in results:
	content = urllib2.urlopen(result['url']).read()
	soup = BeautifulSoup(content)
	images = soup.find_all("img")
	if images is None:
		continue
	for image in images:
		search_result = {}
		search_result['page-url'] = result['url']
		search_result['title'] = result['title']
		search_result['image-url'] = (result['url']+image['src']).replace('\n','')
		data['images'].append(search_result)

json_data = json.dumps(data)
print json_data