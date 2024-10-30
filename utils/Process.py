from bs4 import BeautifulSoup
from utils import HTMLCollector
from utils import MetaCollector
from utils import TextCollector
from utils import UrlPuller
import os
import requests

class Process:
    """Takes in a text file of URLs then loops through them, 'processing' each one"""

    def __init__(self, url_list_file):
        """Pass in the list.txt of URLs you want to be processed"""
        self.puller = UrlPuller(url_list_file)

    def log_processed_url(self, url):
        """Save list of processed URLs to txt file in data/processed"""
        with open("./data/processed/processed.txt", "a") as file:
            file.write(url + '\n')

    def make_soup_object(self, page):
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def make_thread_directory(self, id):
        """Creates a new folder to associate with the thread being processed"""
        self.thread_folder_path = "./data/" + id
        os.makedirs(self.thread_folder_path, exist_ok=True)

    def process_current_list(self):
        """For each URL in the list, get thread HTML, metadata JSON, and content JSON"""

        for i in range(self.puller.get_size()):
            # Gets page from URL and makes a new directory for the thread
            url = self.puller.get_url()
            page = requests.get(url, stream=True)  
            soup = self.make_soup_object(page)
            
            intro_element = soup.find(class_="intro")
            
            if intro_element is not None:
                threadNumber = intro_element.get("id")
                self.make_thread_directory(threadNumber)
                
            else:
                threadNumber = soup.find(class_="intro").get("id")

            # HTML file
            thread = HTMLCollector(soup, self.thread_folder_path)
            (thread.saveHTML())

            # JSON metadata file
            meta = MetaCollector(page, soup, self.thread_folder_path)
            (meta.meta_dump())

            # JSON thread content file
            content = TextCollector(soup, self.thread_folder_path)
            (content.write_thread())

            # Add URL to list of processed URLs
            self.log_processed_url(url)

            self.puller.next_url()