#Import pprint

# Import request and beautiful soup
import requests
from bs4 import BeautifulSoup

#get the response back from the URL

res = requests.get('https://news.ycombinator.com/news')
#soup
soup = BeautifulSoup(res.text, 'html.parser')

