import requests

URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

print(page.text)