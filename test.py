import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = '/Users/lucasrodriguez/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.implicitly_wait(10)

driver.get('https://www.nbcsports.com/bayarea/giants')

#ARTICLE 1
title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/section/div/div[1]/a[1]/div/p[1]/span[1]').text

article = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/section/div/div[1]/a[1]')
article.send_keys(webdriver.common.keys.Keys.RETURN)


link = driver.current_url

print(title)
print(link)





driver.quit()
