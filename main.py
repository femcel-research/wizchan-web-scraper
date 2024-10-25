import requests
from bs4 import BeautifulSoup
from utils import TextCollector

# from utils import Webcopy
from utils import UrlPuller
from utils import HTMLCollector
from utils import MetaCollector

# Website URL
# URL = "https://crystal.cafe/b/res/293815.html#294827"
# URL = "https://crystal.cafe/b/res/294499.html#q294499"
# URL = "https://crystal.cafe/b/res/140376.html#q140376"
# URL = "https://crystal.cafe/feels/res/63992.html#116946"
URL = "https://crystal.cafe/b/res/273609.html#295472"
#URL = "https://crystal.cafe/b/res/295503.html#q295503"

page = requests.get(URL, stream=True)

# Saves text from page in a .txt file named after the string arg
textCollector = TextCollector(page)
textCollector.write_thread()

# Saves local copy of url and stores in a folder named after thread number COLLECTS IMAGES DONT USE FOR NOW
# webCopy = Webcopy(URL, threadNumber)
# pageCopy = webCopy.save_to_html()
# (pageCopy)

# HTMLCollection = HTMLCollector(page)
# saveHTML = HTMLCollection.saveHTML()
# (saveHTML)

# metaCollector = MetaCollector(page)
# dump = metaCollector.meta_dump()
# (dump)
