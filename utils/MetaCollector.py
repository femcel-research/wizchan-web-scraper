from htmldate import find_date
import json
import requests
import datetime
import os

class MetaCollector:
    def __init__(self, URL, pageName):
        self.URL = URL
        self.pageName = pageName

    def dateToJSON(self):
        """Captures date metadata from a specified website and dumps it into a JSON file"""
        #File path
        folder_path = './web-scraper/data/meta'
        file_name = "thread_" + self.pageName + ".json"
        file_path = os.path.join(folder_path, file_name) 

        #Obtains website
        url = self.URL
        response = requests.get(url)

        #Uses htmldate lib to find original and update dates
        publish_Date = find_date(response.content, extensive_search=True, original_date= True)
        update_Date = find_date(response.content, extensive_search= False, original_date= False)
        
        #Assumption is that each time this func is run during scrape, it will capture the time at that moment
        scrape_date = datetime.datetime.now()
        formatted_date = scrape_date.strftime('%Y-%m-%d')

        dates = {
            "date published": publish_Date,
            "date updated": update_Date,
            "date scraped": formatted_date
            }
        
        with open(file_path, "w",  encoding='utf-8') as f:
            json.dump(dates, f, indent=2, ensure_ascii=False)
        

