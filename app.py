from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os


browser = webdriver.Firefox()
browser.get('http://www.tippmix.hu/sportfogadas#?sportid=1')
print("Hope it works")
elements = browser.find_element_by_class_name('table-default').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
elements.pop()
for element in elements:

    print(element.find_element_by_class_name('nums').get_attribute('innerHTML'))
    print(element.find_element_by_class_name('title').get_attribute('innerHTML'))
    print(element.find_element_by_class_name('market').get_attribute('innerHTML'))

browser.close()
