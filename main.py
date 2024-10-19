import requests
from bs4 import BeautifulSoup
from utils import TextSaver

# from utils import Webcopy
from utils import UrlPuller
from utils import WebpageSaver
from utils import MetaCollector

# Website URL
# URL = "https://crystal.cafe/b/res/293815.html#294827"
# URL = "https://crystal.cafe/b/res/294499.html#q294499"
# URL = "https://crystal.cafe/b/res/140376.html#q140376"
# URL = "https://crystal.cafe/feels/res/63992.html#116946"
# URL = "https://crystal.cafe/b/res/273609.html#295472"
URL = "https://crystal.cafe/b/res/295503.html#q295503"

page = requests.get(URL, stream=True)

# Creates a soup object.
soup = BeautifulSoup(page.content, "html.parser")

# Returns top portion of original post
threadIntro = soup.find(class_="intro")

# Should hopefully always return the thread number, given that for crystal.cafe, the thread number is always the first id in the intro class
threadNumber = soup.find(class_="intro").get("id")

# Finds the first instance of a page element with the class "body".
# Within a specific thread page, this most likely be the original thread.
originalPost = soup.find(class_="post op")

# Variable holds the ID of the original post.
originalPostID = threadIntro["id"]

# Finds every page element with the class "post reply" and returns it in an array.
postReplies = soup.find_all(class_="post reply")

# Returns an array containing the ID for each reply.
postReplyIds = [reply["id"] for reply in postReplies]

# Returns an array containing all of the image data for post images
allImages = soup.find_all("img", class_="post-image")

# Returns the sources for each post image
imageSources = [image["src"] for image in allImages]

# Returns imageboard name
board = soup.header.h1.get_text()

# TODO dateCollected is captured in the HTML file when local files are downloaded, time is in UTC

# Saves text from page in a .txt file named after the string arg
# textSaver = TextSaver("testfile.txt", originalPost, postReplies, threadNumber)
# saveText = textSaver.write_thread()
# (saveText)

# Saves local copy of url and stores in a folder named after thread number
# webCopy = Webcopy(URL, threadNumber)
# pageCopy = webCopy.save_to_html()
# (pageCopy)

# webpageSaver= WebpageSaver(URL, threadNumber)
# savePage = webpageSaver.saveHTML()
# (savePage)

metaCollector = MetaCollector(URL, threadNumber)
dump = metaCollector.meta_dump()
(dump)
