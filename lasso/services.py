from lasso.data.mongo import LinkDao

class LinkService(object):

    def __init__(self, dao):
        self.dao = LinkDao()

    def save_link(self, link):
        self.dao.save(link)

    def links_with_tag(self, tag):
        return self.dao.tag_search(tag)