from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os



class HTMLCollector:
    """Saves a URL's HTML into a file"""
    def __init__(self, page):
        self.page = page

    def saveHTML(self):
        """Saves HTML"""
        soup = BeautifulSoup(self.page.content, "html.parser")
        # Should hopefully always return the thread number, given that for crystal.cafe, the thread number is always the first id in the intro class
        threadNumber = soup.find(class_="intro").get("id")
        
        folder_path = './web-scraper/data/HTML'
        file_name = "thread_" + threadNumber + ".html"
        file_path = os.path.join(folder_path, file_name) 

        
        with open(file_path, "w") as f:
            f.write(soup.prettify())