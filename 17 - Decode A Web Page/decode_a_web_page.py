import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content)

soup.prettify()

for tag in soup.find_all("h2"):
    print(tag)
