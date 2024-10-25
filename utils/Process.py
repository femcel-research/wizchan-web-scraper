from bs4 import BeautifulSoup
import HTMLCollector
import MetaCollector
import TextCollector
import UrlPuller
import os
import requests

class Process:
    """Takes in a text file of URLs then loops through them, 'processing' each one"""

    def __init__(self, url_list_file):
        self.puller = UrlPuller.UrlPuller(url_list_file)

    # Save list of processed URLs to txt file
    def log_processed_url(url):
        with open("./web-scraper/data/processed/processed.txt", "a") as file:
            file.write(url + '\n')

    def get_soup_object(page):
        soup = BeautifulSoup(page.page.content, "html.parser")
        return soup

    def make_thread_directory(id):
        thread_folder_path = "./web-scraper/data/" + id
        os.mkdir(thread_folder_path)

    def process_current_list(self):
        # For each URL
        for i in range(self.puller.get_size()):
            # Gets page from URL and makes a new directory for the thread
            url = self.puller.get_url
            page = requests.get(url, stream=True)  
            id = self.get_soup_object(page).find(class_="intro").get("id")
            self.make_thread_directory(id)

            # HTML file
            HTMLCollection = HTMLCollector(page)
            HTMLCollection.saveHTML()

            # JSON metadata file
            metaCollector = MetaCollector(page)
            metaCollector.meta_dump()

            # JSON thread content file
            textSaver = TextCollector("testfile.txt", page)
            textSaver.write_thread()

            # Add URL to list of processed URLs
            self.log_processed_url(url)

            self.puller.next_url