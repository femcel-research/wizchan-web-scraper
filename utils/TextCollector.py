from bs4 import BeautifulSoup
import requests
import json
import os
import re 
  
class TextCollector:
    #TODO maybe save relevant text as .JSON?
    
    def __init__(self, soup, folder_path):
        
        # Creates a soup object.
        self.soup = soup

        # Returns top portion of original post
        self.threadIntro = soup.find(class_="intro")
        self.threadNumber = soup.find(class_="intro").get("id")

        # Finds the first instance of a page element with the class "body".
        # Within a specific thread page, this most likely be the original thread.
        self.originalPost = soup.find(class_="post op")

        # Variable holds the ID of the original post.
        self.originalPostID = self.threadIntro["id"]

        # Finds every page element with the class "post reply" and returns it in an array.
        self.postReplies = soup.find_all(class_="post reply")

        # Returns an array containing the ID for each reply.
        postReplyIds = [reply["id"] for reply in self.postReplies]

        # Returns an array containing all of the image data for post images
        self.allImages = soup.find_all("img", class_="post-image")

        # Returns the sources for each post image
        imageSources = [image["src"] for image in self.allImages]

        # Returns imageboard name
        board = soup.header.h1.get_text()
        
        self.folder_path = folder_path        
        self.file_name = "content_" + self.threadNumber + ".json"
        self.file_path = os.path.join(self.folder_path, self.file_name)
    

    def write_thread(self):
        """Opens a writeable text file, writes related headers and original post content on it and then closes file."""
        threadContents = {
            "thread number": self.threadNumber,
        }
        
        
        original_post_body = self.originalPost.find(class_="body")
        links_to_other_posts = original_post_body.find_all('a', attrs={'href': re.compile("^/")})
        links = []
        
        original_content = {
            "post id": self.originalPost.find(class_="intro").get("id"),
            "username":  self.originalPost.find(class_="name").get_text(),
            "reply to another thread?": True if links else False,
            "date posted": self.originalPost.find(class_="post_no date-link").get("title"),
            "post content": original_post_body.get_text() 
        }
        
        if links:
            original_content["replied thread links"] = links
        
        threadContents["original post"] = original_content
        
        
        for reply in self.postReplies:
            reply_body = reply.find('div', class_= "body")
            links_to_other_posts = reply_body.find_all('a', attrs={'href': re.compile("^/")})
            links = []
            for link in links_to_other_posts:
                links.append(link.get('href'))
            
            reply_content = {
                 "reply id": reply.find(class_="intro").get("id"),
                 "replied post links": links,
                 "username":  reply.find(class_="name").get_text(),
                 "date posted": reply.find(class_="post_no date-link").get("title"),
                 "post content": reply_body.get_text()
             }
            
            threadContents[reply["id"]] = reply_content
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(threadContents, f, indent=3, ensure_ascii=False)