import requests
from bs4 import BeautifulSoup

URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

#Creates a soup object.
soup = BeautifulSoup(page.content, "html.parser")

#Finds the first instance of a page element with the class "body". Within a specific thread page, this most likely be the original thread.
threadContents = soup.find(class_= "body")

#Prints the text from the original thread content, excluding the HTML tags.
print("Original Thread Content: " + threadContents.get_text() + '\n')

#Finds every page element with the class "post reply" and returns it in an array.
print("Replies:")
threadReplies = soup.find_all(class_= "post reply") 

#For each reply in the array, the text is taken from the array element and printed. Thus excluding the HTML tags.
for reply in threadReplies:
    print(reply.get_text())

