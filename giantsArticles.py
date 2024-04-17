import re
import tweepy
import requests
from bs4 import BeautifulSoup
from lxml import etree

API_KEYS_FILE = "api_keys.txt"
DB_FILE = "history.txt"

class Article:
	title: str
	link: str

	def __init__(self, t, l):
		self.title = t
		self.link = l
class Website:
	name: str
	link: str
	title_xpath: str
	link_xpath: str

	def __init__(self, n, l, atx, alx):
		self.name = n
		self.link = l
		self.title_xpath = atx
		self.link_xpath = alx

sites = [
	Website("The Athletic", "https://theathletic.com/team/sf-giants", '//*[@id="body-container"]/div[3]/div/div/div[1]/div/div/a/div/span/div[2]/div[1]/div/h4/span', '//*[@id="body-container"]/div[3]/div/div/div[1]/div/div/a'),
	Website("SF Chronicle", "https://www.sfchronicle.com/sports/giants", '', ''),
	Website("NBCS Bay Area", "https://www.nbcsports.com/bayarea/giants", '', ''),
	Website("KNBR", "https://www.knbr.com/giantsnews", '', ''),
	Website("Around The Foghorn", "https://aroundthefoghorn.com", '', ''),
]

def get_latest_article(website: Website) -> Article:
	home = requests.get(website.link)
	content = BeautifulSoup(home.content, 'html.parser')
	parsed_content = etree.HTML(str(content))
	
	title = ""
	element = parsed_content.xpath(website.title_xpath)
	while len(element) > 0:
		title += element[0].text
		element = element[0].getchildren()

	link = ""
	element = parsed_content.xpath(website.link_xpath)
	if len(element) > 0:
		article_link = element[0].get('href')
		if not ("http" in article_link):
			link = website.link + article_link
		else:
			link = article_link
	
	if title == "" or link == "":
		return None
	
	return Article(title, link)

def already_posted(article: Article, history: dict) -> bool:
	# TODO
	return False

def read_history() -> dict:
	# TODO
	return

def write_history(history: dict):
	# TODO
	return

def get_api():
	apiKeys = open(API_KEYS_FILE, "r")
	keys = apiKeys.readlines()
	keys = [x.strip() for x in keys]

	#SET API KEYS
	auth = tweepy.OAuthHandler(keys[0], keys[1])

	#SET ACCESS TOKENS
	auth.set_access_token(keys[2], keys[3])

	#CREATE API INSTANCE
	api = tweepy.API(auth)
	return api

def post(article, api):
	# TODO
	return

def main():
	history = read_history()
	x_api = get_api()
	for site in sites:
		try:
			article = get_latest_article(site)
			if article == None:
				continue
			if already_posted(article, history):
				continue
			post(article, x_api)
		except Exception as e:
			print("Encountered an error while processing", site.name, ":", type(e).__name__, "-", e)
	write_history(history)
	return 0
	
if __name__ == "__main__":
    main()
