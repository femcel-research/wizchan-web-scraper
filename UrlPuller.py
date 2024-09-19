class UrlPuller:
    """Extracts URLs from a text file"""
    
    def __init__(self, filename):
        filename = ""
        self.filename = filename
        self.url_list = []
        self.url_index = 0
        with open(self.filename, 'r') as file:
            for line in file:
                self.url_list.extend(line)

    def next_url(self):
        self.url_index+=1

    def get_url(self):
        return self.url_list[self.url_index]
    
    def get_size(self):
        return len(self.url_list)
    