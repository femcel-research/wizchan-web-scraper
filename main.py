import requests
from bs4 import BeautifulSoup

URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#print(page.text)
print(soup.prettify())