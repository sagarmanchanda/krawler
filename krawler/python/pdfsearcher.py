#!/usr/bin/env python

from whoosh import index
from whoosh import qparser 
import sys
import json
import re

cmdargs = sys.argv

ix = index.open_dir("/opt/lampp/htdocs/web/python/pdf-indexdir")

searcher = ix.searcher()
result_dict = {}

serach_term = ""
dump = 0
for arg in cmdargs:
	if dump != 0:
		serach_term = serach_term + str(arg) + " "
	dump += 1

serach_term = unicode(serach_term, "utf-8")

qp = qparser.QueryParser("content", ix.schema)
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
	split_link = re.split(r'[:~/\s\n]\s*', result['url'])
	name = ""
	for string in split_link:
		if string.endswith(".pdf") is True:
			name = string
	if name == "":
		name = "Unknown Name"
	name = name.upper()

	search_result = {}
	search_result['url'] = result['url']
	search_result['title'] = name
	data['results'].append(search_result)

json_data = json.dumps(data)
print json_data