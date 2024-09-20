class TextSaver:
    def __init__(self, filename):
        self.filename = filename
    # Opens a writeable text file, writes related headers and original post content on it and then closes file.
    def write_original_post(self, originalPost):
        with open(self.filename, 'w', encoding='utf-8') as outputFile:
            outputFile.write("Original Post: " + '\n')
            outputFile.write(originalPost.get_text() + '\n\n')
            outputFile.write("Replies:" + '\n')

# For each reply in the array, the text is taken from the array element and appended into an open text file. 
# HTML tags are excluded, and the file is closed once the code is executed.
    def write_post_replies(self, postReplies):
        for reply in postReplies:
            with open(self.filename, 'a', encoding='utf-8') as outputFile:
                outputFile.write(reply.get_text() + '\n')

    def write_thread(self, originalPost, postReplies):
         self.write_original_post(originalPost)
         self.write_post_replies(postReplies)

# Opens, prints contents of text file in terminal for debugging, and then closes the file once code is executed.
    def print_file_in_terminal(self):
        with open(self.filename, 'r', encoding='utf-8') as outputFile:
                print(outputFile.read())