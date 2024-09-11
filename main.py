import requests
from bs4 import BeautifulSoup

URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
threadContents = soup.find(class_= "body")

#still working on printing all thread replies
threadReplies = soup.find_all('div', class_= "post reply")

print(threadContents.prettify())
#print(threadReplies.prettify())

#for replies in threadReplies:
    #replyContents = threadReplies.find_all('div', class_="body")

    #for comment in replyContents:
        #print(comment.text())

#print(page.text)
#print(soup.prettify())
