#Webscraper to get my image from my personal website Using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

html = urlopen("file:///C:/Users/ASUS/Documents/wonah/wonah-web-developer/index.html")
my_url = (html.read())
#print(my_url)

bs = soup(my_url, 'html.parser')

image = bs.find('img', {"id":"image"})

#Accessing Attributes of the image tag in my website

print(image.attrs['src'])
print(image.attrs['height'])
print(image.attrs['width'])

#Using Lambda functions in webscraping

only2 = bs.find_all(lambda tag: len(tag.attrs) == 3)

print(only2)