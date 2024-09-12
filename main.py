import requests
from bs4 import BeautifulSoup

URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

#Creates a soup object.
soup = BeautifulSoup(page.content, "html.parser")

#Finds the first instance of a page element with the class "body". Within a specific thread page, this most likely be the original thread.
originalPost = soup.find(class_= "post op")

with open('testfile.txt', 'w', encoding='utf-8') as outputFile:
    outputFile.write("Original Post: " + '\n')
    outputFile.write(originalPost.get_text() + '\n\n')
    outputFile.write("Replies:" + '\n')


#Prints the text from the original thread content, excluding the HTML tags.
#print("Original Post: " + '\n' + originalPost.get_text() + '\n')

#Finds every page element with the class "post reply" and returns it in an array.
postReplies = soup.find_all(class_= "post reply") 

#For each reply in the array, the text is taken from the array element and printed. Thus excluding the HTML tags.
for reply in postReplies:
    #print(reply.get_text())
    with open('testfile.txt', 'a', encoding='utf-8') as outputFile:
        outputFile.write(reply.get_text() + '\n')

with open('testfile.txt', 'r', encoding='utf-8') as outputFile:
        print(outputFile.read())

