#!/usr/bin/env python

from whoosh import index
from whoosh import qparser 
import sys
import json

cmdargs = sys.argv

ix = index.open_dir("/opt/lampp/htdocs/web/python/form-indexdir")

searcher = ix.searcher()

serach_term = ""
dump = 0
for arg in cmdargs:
	if dump != 0:
		serach_term = serach_term + str(arg) + " "
	dump += 1

serach_term = unicode(serach_term, "utf-8")

qp = qparser.QueryParser('title', ix.schema)
q = qp.parse(serach_term) 	
results = searcher.search(q)


data = {}
data['results'] = []
data['didyoumean'] = ""

if len(results) == 0:
	corrected = searcher.correct_query(q, serach_term)
	if corrected.query != q:
	     data['didyoumean'] = corrected.string

for result in results:
	search_result = {}
	search_result['title'] = result['title']
	search_result['pdf_url'] = result['pdf_url']
	search_result['doc_url'] = result['doc_url']
	data['results'].append(search_result)

json_data = json.dumps(data)
print json_data
