from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os



class HTMLCollector:
    """Saves a URL's HTML into a file"""
    def __init__(self, URL, pageTitle):
        self.URL = URL
        self.pageTitle = pageTitle

    def saveHTML(self):
        """Saves HTML"""
        folder_path = './web-scraper/data/HTML'
        file_name = "thread_" + self.pageTitle + ".html"
        file_path = os.path.join(folder_path, file_name) 

        session = HTMLSession()
        response = session.get(self.URL)
        soup = BeautifulSoup(response.content, "html.parser")
        
        with open(file_path, "w") as f:
            f.write(soup.prettify())