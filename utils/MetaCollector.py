from htmldate import find_date
from bs4 import BeautifulSoup
import json
import requests
import datetime
import os


class MetaCollector:
    """Collects metadata from a website and stores it in a JSON file"""

    def __init__(self, URL, pageName):
        # Website info
        self.URL = URL
        self.pageName = pageName
        self.response = requests.get(self.URL)

        # File path
        self.folder_path = "./web-scraper/data/meta"
        self.file_name = "thread_" + self.pageName + ".json"
        self.file_path = os.path.join(self.folder_path, self.file_name)

    def date_to_JSON(self):
        """Captures date published, date updated, and date scraped from a specified website"""

        # Uses htmldate lib to find original and update dates
        publish_Date = find_date(
            self.response.content, extensive_search=True, original_date=True, outputformat= "%Y-%m-%d %H:%M:%S"
        )
        update_Date = find_date(
            self.response.content, extensive_search=False, original_date=False, outputformat= "%Y-%m-%d %H:%M:%S"
        )

        # Assumption is that each time this func is run during scrape, it will capture the time of scrape
        scrape_date = datetime.datetime.now()
        formatted_date = scrape_date.strftime("%Y-%m-%d %H:%M:%S")

        dates = {
            "date published": publish_Date,
            "date updated": update_Date,
            "date scraped": formatted_date,
        }

        return dates

    def page_info_to_JSON(self):
        """Captures page URL, title, description, keywords, site info"""

        page = requests.get(self.URL, stream=True)
        soup = BeautifulSoup(page.content, "html.parser")

        # If meta keywords has content create a variable with that content, otherwise set to empty string
        meta_keywords = soup.find("meta", attrs={"name": "keywords"})
        if meta_keywords:
            keywords = meta_keywords["content"]
        else:
            keywords = ""

        # If meta description has content create a variable with that content, otherwise set to empty string
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description:
            description = meta_description["content"]
        else:
            description = ""

        info = {
            "URL": page.url,
            "board": soup.title.string,  # for cc its safe to assume each title will be the board name
            "thread number": soup.find(class_="intro").get("id"),
            "description": description,
            "keywords": keywords,
        }
        return info

    def meta_dump(self):
        """Dumps website metadata into a JSON file"""
        metadata = {**self.page_info_to_JSON(), **self.date_to_JSON()}

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
