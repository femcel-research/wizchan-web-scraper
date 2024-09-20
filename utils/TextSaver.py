class TextSaver:
    def __init__(self, filename, originalPost, postReplies, threadNumber):
        self.filename = filename
        self.originalPost = originalPost
        self.postReplies = postReplies
        self.threadNumber = threadNumber
    
# Opens a writeable text file, writes related headers and original post content on it and then closes file.
    def write_original_post(self):
        with open(self.filename, 'w', encoding='utf-8') as outputFile:
            outputFile.write("Thread Number: " + self.threadNumber + '\n')
            outputFile.write("Original Post: " + '\n')
            outputFile.write(self.originalPost.get_text() + '\n\n')
            outputFile.write("Replies:" + '\n')

# For each reply in the array, the text is taken from the array element and appended into an open text file. 
# HTML tags are excluded, and the file is closed once the code is executed.
    def write_post_replies(self):
        for reply in self.postReplies:
            with open(self.filename, 'a', encoding='utf-8') as outputFile:
                outputFile.write(reply.get_text() + '\n')

    def write_thread(self):
         self.write_original_post()
         self.write_post_replies()

# Opens, prints contents of text file in terminal for debugging, and then closes the file once code is executed.
    def print_file_in_terminal(self):
        with open(self.filename, 'r', encoding='utf-8') as outputFile:
                print(outputFile.read())