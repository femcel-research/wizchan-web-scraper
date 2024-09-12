import requests
from bs4 import BeautifulSoup

# Website URL
URL = "https://crystal.cafe/b/res/293815.html#294827"
page = requests.get(URL)

# Creates a soup object.
soup = BeautifulSoup(page.content, "html.parser")

# Finds the first instance of a page element with the class "body". 
# Within a specific thread page, this most likely be the original thread.
originalPost = soup.find(class_= "post op")

# Opens a writeable text file, writes related headers and original post content on it and then closes file.
with open('testfile.txt', 'w', encoding='utf-8') as outputFile:
    outputFile.write("Original Post: " + '\n')
    outputFile.write(originalPost.get_text() + '\n\n')
    outputFile.write("Replies:" + '\n')

# Finds every page element with the class "post reply" and returns it in an array.
postReplies = soup.find_all(class_= "post reply") 

# For each reply in the array, the text is taken from the array element and appended into an open text file. 
# HTML tags are excluded, and the file is closed once the code is executed.
for reply in postReplies:
    with open('testfile.txt', 'a', encoding='utf-8') as outputFile:
        outputFile.write(reply.get_text() + '\n')

# Opens, prints contents of text file in terminal for debugging, and then closes the file once code is executed.
with open('testfile.txt', 'r', encoding='utf-8') as outputFile:
        print(outputFile.read())

