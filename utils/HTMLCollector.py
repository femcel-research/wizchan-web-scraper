from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os


#TODO no longer need to pass page
class HTMLCollector:
    """Saves a URL's HTML into a file"""
    def __init__(self, soup, id, folder_path):
        self.soup = soup
        self.id = id
        self.folder_path = folder_path

    def saveHTML(self):
        """Saves HTML"""
        file_name = "thread_{}.html".format(self.id)
        file_path = os.path.join(self.folder_path, file_name) 
        
        with open(file_path, "w") as f:
            f.write(self.soup.prettify())