import requests
import re
from urllib.parse import urlparse

class PyCrawler(object):
    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.visited = set()
    
    def get_html(self, url):
        try:
            html = requests.get(url)
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    
    def start():
        pass

if __name__ == "__main__":
    crawler = PyCrawler()
    crawler.start()
