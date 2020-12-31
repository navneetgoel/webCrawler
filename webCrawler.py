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
    
    def get_links(self, url):
        html = self.get_html(url)
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)
        for i, link in enumerate(links):
            if not urlparse(link).netloc:
                link_with_base = base + link
                links[i] = link_with_base
        
        return set(filter(lambda x: 'mailto' not in x, links))
    
    def extract_info(self, url):
        html = self.get_html(url)
        return None
    

    
    def start():
        pass

if __name__ == "__main__":
    crawler = PyCrawler()
    crawler.start()
