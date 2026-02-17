from bs4 import BeautifulSoup
import requests
class NewsScraper:

    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def fetch(self):
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        headlines = soup.find_all("h2")
        return [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

    def save(self, headlines, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(headlines))


scraper = NewsScraper("https://www.bbc.com/")
html = scraper.fetch()
headlines = scraper.parse(html)
scraper.save(headlines, "headlines.txt")
