'''Using Regular Expression to get image src ending with png from website'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

master_list = []

html = urlopen("file:///C:/Users/ASUS/Documents/wonah/wonah-web-developer/index.html")

soup = BeautifulSoup(html, 'html.parser')

#print(soup)

images = soup.find('img', {'src': re.compile('image\/[A-Za-z0-9]*\.png')})

for image in images:
    master_list.append(image)

print(master_list)
