import requests
import os
from bs4 import BeautifulSoup
from pywebcopy import save_webpage
import UrlPuller
import WebCopy
from TextSaver import TextSaver

# Website URL
#URL = "https://crystal.cafe/b/res/293815.html#294827"
URL = "https://crystal.cafe/b/res/294499.html#q294499"
page = requests.get(URL, stream = True)

# Creates a soup object.
soup = BeautifulSoup(page.content, "html.parser")

# Returns top portion of original post
threadIntro = soup.find(class_="intro")

#Should hopefully always return the thread number, given that for crystal.cafe, the thread number is always the first id in the intro class
threadNumber = soup.find(class_= "intro").get('id')

# Finds the first instance of a page element with the class "body". 
# Within a specific thread page, this most likely be the original thread.
originalPost = soup.find(class_= "post op")

# Variable holds the ID of the original post.
originalPostID= threadIntro['id']

# Finds every page element with the class "post reply" and returns it in an array.
postReplies = soup.find_all(class_= "post reply")

# Returns an array containing the ID for each reply.
postReplyIds = [reply['id'] for reply in postReplies]

# Returns an array containing all of the image data for post images
allImages = soup.find_all('img', class_="post-image")

# Returns the sources for each post image
imageSources = [image['src'] for image in allImages]

# Returns imageboard name
board = soup.header.h1.get_text()

#TODO dateCollected = 

# Saves text from page in a .txt file named after the string arg
textSaver = TextSaver("testfile.txt")
saveText = textSaver.write_thread(originalPost, postReplies)
(saveText)

# Saves local copy of url and stores in a folder named after thread number
#pageCopy = WebCopy.save_webpage(URL, threadNumber)

#(pageCopy)