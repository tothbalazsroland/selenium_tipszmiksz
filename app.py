from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os


browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')
print "Iam trying not to fuck up this one"