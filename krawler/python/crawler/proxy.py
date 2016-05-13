from bs4 import BeautifulSoup
import urllib.request as req
from searcher import bfs
proxy = req.ProxyHandler({'http': r'http://172.16.115.40:8080'})
auth = req.HTTPBasicAuthHandler()
opener = req.build_opener(proxy,auth,req.HTTPHandler)
req.install_opener(opener)