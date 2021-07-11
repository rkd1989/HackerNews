#Import pprint
import pprint

#Import request and beautiful soup
import requests
from bs4 import BeautifulSoup

#get the response back from the URL
res = requests.get('https://news.ycombinator.com/news')

#parse the content into HTML
soup = BeautifulSoup(res.text, 'html.parser')

# Get the Links and the points
links = soup.select('.storylink')
points = soup.select('.subtext')

#sorts the news stories by score
def sort_scraped_data(ins):
    return sorted(ins, key= lambda k: k['score'], reverse=True)

#filters and stores scraped data in desirable format
def store_scraped_data(links,points):
    consolidated_list = []
    for count, item in enumerate(links):
        if len(points[count].select('.score')) > 0:
            news_dict = {}
            news_dict['title'] = item.getText()
            news_dict['link'] = links[count].get("href", None);
            news_dict['score'] = int(points[count].select('.score')[0].getText().replace(" points", ""))
            consolidated_list.append(news_dict)
    return sort_scraped_data(consolidated_list)

#pretty print the results
pprint.pprint(store_scraped_data(links,points))

