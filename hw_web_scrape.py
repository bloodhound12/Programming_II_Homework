
import requests
from bs4 import BeautifulSoup
url = "https://softwarica.edu.np/"
# step 1: Get the HTML
r = requests.get(url) 
htmlcontent = r.content
# print(htmlcontent)

# step 2: Parse the html 
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)

# step 1: html tree traversal 
# print(type(soup.title)) # tag
# print(type(soup.title.string)) # navigable string
# title = soup.title

# Get all the paragraphes from the page 
paras = soup.find_all('p')
print(paras)