'''
Methods to scrape a website:
    1. Use the API
    2. Use some web scraping tool like beautifulsoup
'''

'''
Step 0: Install all the requirements
    - install beautifilsoup (pip install beautifulsoup4)
    - install requests library (pip install requests)
    - install some parsing library (pip install lxml)
'''

# Step 1: import the necessary libraries and the url of the site to scrape
import requests
from bs4 import BeautifulSoup as bs
url = "https://codewithharry.com"

# Step 2: Get the html content
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 3 : Prepare a soup (Parse the html)
soup = bs(htmlContent, 'lxml')
# print(soup.prettify())

# Step 4: Traverse the html tree
# Commonly used types of objects
#1. Tag
#2. NavigableString
#3. BeautifulSoup
#4. Comment

title = soup.title # get the title of the html tag
# print(type(soup))
# print(type(title))
# print(type(title.text))

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags from the page
anchors = soup.find_all('a')
for anchor in anchors:
    print(anchor.text)


