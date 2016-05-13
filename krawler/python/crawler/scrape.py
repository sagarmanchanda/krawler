import proxy
import queue
from bs4 import BeautifulSoup
import urllib.request as req
from searcher import bfs
import hashlib

god_list=[]
queue_link = queue.Queue()
hash = []

def scrape(url):
	queue_link.put(url)
	while not queue_link.empty():
		find_url(queue_link.get())
	

def find_url(url):
	try:
		page = req.urlopen(url)
	except:
		print("URL can not be opened.\n")
		return
	file_type = page.info()['Content-Type']
	try:
		if "text/html" in file_type:
			content = page.read()
			hash_val = hashlib.sha224(content).hexdigest()
			if hash_val not in hash:
				hash.append(hash_val)
				f = open('links.txt','a')
				f.write(url+'\n')
				f.close()
				if 'iitg.ernet' in url:
					soup = BeautifulSoup(content)
					print("reached here")
					print(type(soup))
					links = bfs(soup)
					print(links)
					print("populated links!")
					populate_god(links)
					# call @Sagar manchanda's function to index html links here
			# valid link to go through
		else:
			file_type = file_type.replace('/','_')
			f = open('downloadable/'+file_type+'.txt','a')
			f.write(url+'\n')
			f.close()
			#this part needs more work @Sagar manchanda.
				# add link in Downloadable folder in the file corresponding to the filetype. 
	except:
		return
		
def populate_god(links):
	for link in links:
		if link not in god_list:
			god_list.append(link)
			queue_link.put(link)

	
