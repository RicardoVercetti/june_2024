# web_creawling.py
import requests
from bs4 import BeautifulSoup as bs
from utils import save_in_a_file, load_from_the_file


# variables
LOCAL_FILE = "hi_anime_home.txt"
URL = "https://hianime.to/home"




# crawl code
def fetch_from_url(url: str):
	soup = bs(requests.get(url).text, "html.parser")
	# print(soup.prettify())
	# save_in_a_file(soup.prettify(), LOCAL_FILE)

def crawl(data: str):
	soup = bs(data, "html.parser")
	# print(soup.prettify())
	li = soup.find_all("li")
	for i in li:
		print("=======")
		print(i.prettify())



crawl(load_from_the_file(LOCAL_FILE))

