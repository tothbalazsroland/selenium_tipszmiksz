from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os


browser = webdriver.Firefox()
browser.get('http://www.tippmix.hu/sportfogadas')

tippmix_page = BeautifulSoup(browser.page_source, 'lxml')
print tippmix_page.find_all('tbody')[3].get_text()


browser.close()
