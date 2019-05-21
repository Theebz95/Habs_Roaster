import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.nhl.com/canadiens/roster'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

table = page_soup.find('table', {'class':'split-table'})

first_name = page_soup.findAll('span', {'class':'name-col__item name-col__firstName'})
last_name = page_soup.findAll('span', {'class':'name-col__item name-col__lastName'})
for i in range(len(first_name)):
    print(first_name[i])
    print(last_name[i])