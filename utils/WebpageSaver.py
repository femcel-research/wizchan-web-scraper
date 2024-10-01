from selenium import webdriver
import requests
import codecs
import os

class WebpageSaver:
    def __init__(self, URL, pageTitle):
        self.URL = URL
        self.pageTitle = pageTitle

    def saveWebpage(self):
        #set chromedriver.exe path
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        driver.implicitly_wait(0.5)
        #maximize browser
        driver.maximize_window()
        #launch URL
        driver.get(self.URL)
        #get file path to save page
        filePath = os.path.join(".\HTML", self.pageTitle + ".html")
        #open file in write mode with encoding
        file = codecs.open(filePath, "w", "utf−8")
        #obtain page source
        pageSource = driver.page_source
        #write page source content to file
        file.write(pageSource)
        #close browser
        driver.quit()