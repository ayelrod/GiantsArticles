import tweepy
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree

API_KEYS_FILE = "api_keys.txt"
DB_FILE = "history.json"
HEADER = {
    'referer':'https://www.google.com/'
}

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
	# Website("SF Chronicle", "https://www.sfchronicle.com/sports/giants", '//*[@id="__next"]/main/div[4]/div/div/div/div[1]/div/div[2]/h2/a', '//*[@id="__next"]/main/div[4]/div/div/div/div[1]/div/div[2]/h2/a'), # CAPTCHA Protected
	Website("NBCS Bay Area", "https://www.nbcsports.com/bayarea/giants", '//*[@id="main"]/div[2]/div[2]/div[1]/div[2]/div[2]/a', '//*[@id="main"]/div[2]/div[2]/div[1]/div[2]/div[2]/a'),
	# Website("KNBR", "https://www.knbr.com/giantsnews", '//*[@id="wp--skip-link--target"]/div[1]/div[1]/ul/li[1]/div/div[2]/h2/a', '//*[@id="wp--skip-link--target"]/div[1]/div[1]/ul/li[1]/div/div[2]/h2/a'), # Not Working
	Website("Around The Foghorn", "https://aroundthefoghorn.com", '//*[@id="mm-root"]/main/div[2]/section[1]/div/article/div/a', '//*[@id="mm-root"]/main/div[2]/section[1]/div/article/div/a'),
	Website("The Mercury News", "https://www.mercurynews.com/sports/mlb/san-francisco-giants/", '//*[@id="main"]/section/article/div/header/h3/a/span', '//*[@id="main"]/section/article/figure/div/a')
]

def get_latest_article(website: Website) -> Article:
	home = requests.get(website.link, headers=HEADER)
	content = BeautifulSoup(home.content, 'html.parser')
	parsed_content = etree.HTML(str(content))
	
	title = ""
	element = parsed_content.xpath(website.title_xpath)
	while len(element) > 0:
		if element[0].text != None:
			title += element[0].text
		elif element[0].get('title') != None:
			title += element[0].get('title')
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
	
	return Article(title.strip(), link.strip())

def already_posted(site: str, article: Article, history: dict) -> bool:
	if not site in history:
		history[site] = article.link
		return False
	if history[site] == article.link:
		return True
	history[site] = article.link
	return False

def read_history() -> dict:
	try:
		with open(DB_FILE, 'r') as file:
			history = json.load(file)
	except:
		history = {}
	return history

def write_history(history: dict):
	with open(DB_FILE, 'w+') as file:
		json.dump(history, file)
	return

def get_api():
	apiKeys = open(API_KEYS_FILE, "r")
	keys = apiKeys.readlines()
	keys = [x.strip() for x in keys]

	# Create client
	client = tweepy.Client(
    		consumer_key=keys[0],
    		consumer_secret=keys[1],
    		access_token=keys[2],
    		access_token_secret=keys[3]
		)

	return client

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
			if already_posted(site.name, article, history):
				continue
			post(article, x_api)
		except Exception as e:
			print("Encountered an error while processing", site.name, ":", type(e).__name__, "-", e)
	write_history(history)
	return 0
	
if __name__ == "__main__":
    main()
