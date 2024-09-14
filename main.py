import requests
from bs4 import BeautifulSoup
from pywebcopy import save_webpage

# Website URL
#URL = "https://crystal.cafe/b/res/293815.html#294827"
URL = "https://crystal.cafe/b/res/294499.html#q294499"
page = requests.get(URL, stream = True)



# Creates a soup object.
soup = BeautifulSoup(page.content, "html.parser")

#Should hopefully always return the thread number, given that for crystal.cafe, the thread number is always the first id in the intro class
threadNumber = soup.find(class_= "intro").get('id')
#print(threadNumber)

#pywebcopy is a crawler that works to save html, css, and .js from websites to local storage -Moyartu 
#install pywebcopy and lxml[html_clean] package for use.

#Saves a copy of the URL to the HTML folder. Contents are nested in a folder named after the specific thread number.
save_webpage(
    url = URL,
   project_folder = "./HTML",
   project_name = "thread_" + threadNumber,
   bypass_robots=True,
   debug=True,
   open_in_browser=False,
   delay=None,
   threaded = True
)


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

