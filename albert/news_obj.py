class news_obj:
    # constructor: initialize by default
    def __init__(self, title = ''):
        self.title = title

    # print attribute's method
    def print_attr(self):
        print(self.title + '\n')