'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get("https://www.reddit.com/r/wallstreetbets/comments/kw0lin/what_are_your_moves_tomorrow_january_13_2021/")

elements = driver.find_elements_by_css_selector("#md")

print(elements)
'''
#_*_coding: utf-8_*_


# more_t1_gj364dn

from selenium import webdriver
import time

f = open("sel.txt", "w")

print("hi")
browser=webdriver.Firefox()
browser.get("https://old.reddit.com/r/wallstreetbets/comments/kw0lin/what_are_your_moves_tomorrow_january_13_2021/")
time.sleep(2)
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
	# Scroll down to bottom
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# Wait to load page
	time.sleep(SCROLL_PAUSE_TIME)

	# Calculate new scroll height and compare with last scroll height
	new_height = browser.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		browser.execute_script("document.getElementsByClassName('button')[0].click()")
		continue
	last_height = new_height

browser.execute_script("document.getElementsByClassName('button')[0].click()")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
f.write(browser.page_source)

browser.close()
f.close()