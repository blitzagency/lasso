from lasso.utils import AttributeDict

class Link(AttributeDict):
    
    def __init__(self):
        self.url = None
        self.tags = []
        self.created_by = None


    def add_tag(self, tag):
        self.tags.append(tag)