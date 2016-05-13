import proxy
import urllib.request as req
import urllib.parse as parse
import os
downloadable = []

def bfs(soup):
	links = []
	all_links = soup.find_all('a')
	for link in all_links:
		try:
			url = link.get('href')
		except:
			continue
		print(url)
		if 'http' in url:
			links.append(url)
				
	
	return links