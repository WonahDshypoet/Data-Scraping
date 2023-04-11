from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re

html = urlopen("file:///C:/Users/hp/Documents/Sound%20recordings/wonah/index.html")
#bs = soup(html, 'html.parser')

my_url = soup(html.read, 'html.parser')
print(my_url)

my = 2+2
print(my)