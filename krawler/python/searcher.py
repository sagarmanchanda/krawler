#!/usr/bin/env python

from whoosh import index
from whoosh import qparser 
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
results = searcher.search(q, limit=30)


data = {}
data['results'] = []
# data['results']['urls'] = []
# data['results']['title'] = []
data['didyoumean'] = ""

if len(results) == 0:
	corrected = searcher.correct_query(q, serach_term)
	if corrected.query != q:
	     data['didyoumean'] = corrected.string

for result in results:
	searchresult = {}
	searchresult['url'] = result['url']
	searchresult['title'] = result['title']
	data['results'].append(searchresult)

#file = open("result.json","w")
json_data = json.dumps(data)
print json_data
#file.close()