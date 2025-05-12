from html.parser import HTMLParser


class ServiceLinkHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and attr[1].startswith("./list_"):
                    self.links.add(attr[1])

    def handle_endtag(self, tag):
        pass
