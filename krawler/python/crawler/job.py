import proxy
from scrape import scrape
from bs4 import BeautifulSoup
import urllib.request as req
url = "http://intranet.iitg.ernet.in/"
scrape(url)
print("done")