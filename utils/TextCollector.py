from bs4 import BeautifulSoup
import requests
class TextCollector:
    #TODO maybe save relevant text as .JSON?
    
    def __init__(self, page):
        self.page = page
        
        # Creates a soup object.
        soup = BeautifulSoup(page.content, "html.parser")

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
        
        self.folder_path = "./web-scraper/data/thread_contents"        
        self.filename = self.threadNumber + ".txt"
    

    def write_thread(self):
        """Opens a writeable text file, writes related headers and original post content on it and then closes file."""
        originalPost = {
            "thread number": self.threadNumber,
            "original post": self.originalPost.get_text()
        }
        
        for reply in self.postReplies:
             reply_content = {
                 "reply id": reply["id"],
                 "content": reply.get_text()
             }
             originalPost["reply_" + reply["id"]] = reply_content
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(originalPost, f, indent=2, ensure_ascii=False)
        
    # def write_post_replies(self):
    #     """For each reply in the post replies array, the text is taken from the array element and appended into an open text file. 
    #     HTML tags are excluded, and the file is closed once the code is executed."""
        
    #     for reply in self.postReplies:
    #         with open(self.threadNumber, 'a', encoding='utf-8') as outputFile:
    #             outputFile.write(reply.get_text() + '\n')

    # def write_thread(self):
    #      self.write_original_post()
    #      self.write_post_replies()

    # def print_file_in_terminal(self):
    #     """Opens, prints contents of text file in terminal for debugging, and then closes the file once code is executed."""
    #     with open(self.filename, 'r', encoding='utf-8') as outputFile:
    #             print(outputFile.read())