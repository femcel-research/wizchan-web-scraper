import requests
from bs4 import BeautifulSoup

URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
threadContents = soup.find(class_= "body")

print("Original Thread Content: " + threadContents.get_text() + '\n')

#still working on printing all thread replies
print("Replies:")
threadReplies = soup.find_all(class_= "post reply")
for reply in threadReplies:
    print(reply.get_text())




#for replies in threadReplies:
    #replyContents = threadReplies.find_all('div', class_="body")

    #for comment in replyContents:
        #print(comment.text())

#print(page.text)
#print(soup.prettify())
