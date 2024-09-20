import requests
#pywebcopy is a crawler that works to save html, css, and .js from websites to local storage -Moyartu 
#install pywebcopy and lxml[html_clean] package for use.
from pywebcopy import save_webpage

class Webcopy:
    def save_to_html(URL, threadNumber):
        folder = './HTML'
        #Saves a copy of the URL to the HTML folder. Contents are nested in a folder named after the specific thread number.
        save_webpage(
            url = URL,
        project_folder = folder,
        project_name = "thread_" + threadNumber,
        bypass_robots=True,
        debug=True,
        open_in_browser=False,
        delay=None,
        threaded = True #if set to false downloads will be incredibly slow.
        )