'''Using Regular Expression to get image src ending with png from website'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

master_list = []

html = urlopen("file:///C:/Users/hp/Documents/Sound%20recordings/wonah/index.html")

soup = BeautifulSoup(html, 'html.parser')

#print(soup)

images = soup.findAll('img', {'src': re.compile('image\/[A-Za-z0-9]*\.png')})

for image in images:
    master_list.append(image)

print(master_list)
