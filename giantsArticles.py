import re
import tweepy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def main():

	apiKeys = open("api_keys.txt", "r")
	keys = apiKeys.readlines()
	keys = [x.strip() for x in keys]

	#SET API KEYS
	auth = tweepy.OAuthHandler(keys[0], keys[1])

	#SET ACCESS TOKENS
	auth.set_access_token(keys[2], keys[3])

	#CREATE API INSTANCE
	api = tweepy.API(auth)

	#TWEET
	#with open("tweet.txt", "r") as f:
	#	api.update_status(f.read())
	
	#OPEN FILE FOR WRITING
	f = open("tweet.txt", "w+")
	
	#INITIALIZE WEBDRIVER
	DRIVER_PATH = '/Users/lucasrodriguez/Downloads/chromedriver'
	driver = webdriver.Chrome(executable_path=DRIVER_PATH)
	driver.implicitly_wait(10)
	

	#THE ATHLETIC-------------------------------------------------------------------------------------------------
	driver.get('https://theathletic.com/team/sf-giants/')

	f.write('THE ATHLETIC:\n')

	#ARTICLE 1
	title = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[2]/div/a/div[1]').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[2]/div/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')
	
	#ARTICLE 2
	driver.get('https://theathletic.com/team/sf-giants/')

	title = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[3]/div/a/div[2]/div[2]/div/div[1]').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[3]/div/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)	

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')

	f.write('\n@GiantsArticles')
	f.close()
	
	#TWEET
	with open("tweet.txt", "r") as f:
		api.update_status(f.read())

	#SET PREVIOUS TWEET
	prevTweet = api.user_timeline('@GiantsArticles')[0].id
	

	#SF CHRONICLE-------------------------------------------------------------------------------------------------
	f = open('tweet.txt', 'w+')
	driver.get('https://www.sfchronicle.com/sports/giants/')

	f.write('SF CHRONICLE:\n')

	#ARTICLE 1
	title = driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/section/div/div/div/div/div[3]/a').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/section/div/div/div/div/div[3]/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')
	
	#ARTICLE 2
	driver.get('https://www.sfchronicle.com/sports/giants/')

	title = driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/section/div/div/div/ul/li[1]/p/a').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/section/div/div/div/ul/li[1]/p/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')

	f.close()
	
	#TWEET IN THREAD
        with open("tweet.txt", "r") as f:
		api.update_status(f.read(), in_reply_to_status_id=prevTweet)
	

	#MERCURY NEWS-------------------------------------------------------------------------------------------------
	
	#f = open('tweet.txt', 'w+')
	#driver.get('https://www.mercurynews.com/sports/san-francisco-giants/')

	#f.write('MERCURY NEWS:\n')

	#ARTICLE 1
	#title = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/main/section/article/div/header/h2/a/span').text
        #title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	#article = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/main/section/article/div/header/h2/a')
	#article.send_keys(webdriver.common.keys.Keys.RETURN)

	#link = driver.current_url

	#f.write('\n' + title)
	#f.write(': ' + link + '\n')
	
	#ARTICLE 2
	#driver.get('https://www.mercurynews.com/sports/san-francisco-giants/')

	#title = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/main/section[1]/div[2]/article[1]/div[1]/header/h5/a').text
        #title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	#article = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/main/section[1]/div[2]/article[1]/div[1]/header/h5/a')
	#article.send_keys(webdriver.common.keys.Keys.RETURN)

	#link = driver.current_url

	#f.write('\n' + title)
	#f.write(': ' + link + '\n')

	#f.close

	#TWEET
	#with open("tweet.txt", "r") as f:
	#	api.update_status(f.read(), in_reply_to_status_id=prevTweet)

	
	#NBCSBayArea--------------------------------------------------------------------------------------------------
	f = open('tweet.txt', 'w+')
	driver.get('https://www.nbcsports.com/bayarea/giants')
	
	f.write('NBCS Bay Area:\n')
	
	#ARTICLE 1
	title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div/div/div[1]/div/article/div/div[1]/header/div[2]/div/div[1]/a').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div/div/div[1]/div/article/div/div[1]/header/div[2]/div/div[1]/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')
	
	#ARTICLE 2
	driver.get('https://www.nbcsports.com/bayarea/giants')
	
	title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div/div/div[1]/div/article/div/div[1]/header/div[2]/div/div[2]/a').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div/div/div[1]/div/article/div/div[1]/header/div[2]/div/div[2]/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')

	f.close()
	
	#TWEET IN THREAD
        with open("tweet.txt", "r") as f:
		api.update_status(f.read(), in_reply_to_status_id=prevTweet)


	#KNBR---------------------------------------------------------------------------------------------------------
	f = open('tweet.txt', 'w+')
	driver.get('https://www.knbr.com/giantsnews/')

	f.write('KNBR:\n')

	#ARTICLE 1
	article = driver.find_element_by_xpath('/html/body/div[3]/div/section[2]/section[1]/div[2]/div/div[1]/div[1]/article[1]/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	title = driver.find_element_by_xpath('/html/body/div[3]/div/section[2]/section[1]/div[1]/div/div/article/header/h1').text
	title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)
	
	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')

	#ARTICLE 2
	driver.get('https://www.knbr.com/giantsnews')
	
	article = driver.find_element_by_xpath('/html/body/div[3]/div/section[2]/section[1]/div[2]/div/div[1]/div[1]/article[2]/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	title = driver.find_element_by_xpath('/html/body/div[3]/div/section[2]/section[1]/div[1]/div/div/article/header/h1').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)	
	
	link = driver.current_url

        f.write('\n' + title)
        f.write(': ' + link)	

	f.close()
	
	#TWEET IN THREAD
	with open("tweet.txt", "r") as f:
		api.update_status(f.read(), in_reply_to_status_id=prevTweet)

#AroundTheFoghorn-----------------------------------------------------------------------------------------
	
	f = open('tweet.txt', 'w+')
	driver.get('https://aroundthefoghorn.com/')

	f.write('Around The Foghorn:\n')

	#ARTICLE 1
	title = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[1]/div/header/h2/a').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[1]/div/header/h2/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')
	
	#ARTICLE 2
	driver.get('https://aroundthefoghorn.com/')

	title = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[2]/div/header/h2/a').text
        title = re.sub(u"(\xf3|\u2014|\u2018|\u2019|\u2026)", "'", title)

	article = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[2]/div/header/h2/a')
	article.send_keys(webdriver.common.keys.Keys.RETURN)

	link = driver.current_url

	f.write('\n' + title)
	f.write(': ' + link + '\n')

	f.close()	

	#TWEET IN THREAD
	with open("tweet.txt", "r") as f:
		api.update_status(f.read(), in_reply_to_status_id=prevTweet)
	
	driver.quit()	
	
main()
