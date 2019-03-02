from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os


def generate_event(row):
    current_event = Event()
    try:
        current_event.id = row.find('td', {'class': 'nums'}).text.replace('\n', '')
    except AttributeError:
        current_event.id = ''
    try:
        current_event.eventName = row.find('td', {'class': 'title'}).text.replace('\n', '')
    except AttributeError:
        current_event.eventName = ''
    listOfOdds = row.find_all('td', {'class': 'odds'})
    try:
        current_event.home = listOfOdds[0].find('button').text.replace('\n', '')
    except (AttributeError, IndexError):
        print "Did not find button"
        current_event.home = ''
    try:
        current_event.draw = listOfOdds[1].find('button').text.replace('\n', '')
    except (AttributeError, IndexError):
        print "Did not find button"
        current_event.draw = ''
    try:
        current_event.foreign = listOfOdds[2].find('button').text.replace('\n', '')
    except (AttributeError, IndexError):
        print "Did not find button"
        current_event.foreign = ''

    return current_event


def generate_list_of_events_from_page(page):
    table = page.find("div", {'class': 'table-default'}).find('tbody').find_all('tr')
    howmany = len(table) - 1
    print howmany
    listOfEvents = []
    for counter in range(howmany):
        row = table[counter]
        event = generate_event(row)
        listOfEvents.append(event)
    return listOfEvents


class Event:

    def __init__(self):
        self.id = None
        self.eventName = None
        self.home = None
        self.draw = None
        self.foreign = None

    def print_event(self):
        print "Sorszam: " + self.id
        print "Esemeny: " + self.eventName
        print "Hazai: " + self.home
        print "Dontetlen: " + self.draw
        print "Vendeg: " + self.foreign





browser = webdriver.Firefox()
browser.get('http://www.tippmix.hu/sportfogadas')
tippmix_page = BeautifulSoup(browser.page_source, 'lxml')
all_events = []

while len(tippmix_page.find("div", {'class': 'table-default'}).find('tbody').find_all('tr'))==1:
    tippmix_page = BeautifulSoup(browser.page_source, 'lxml')

events = generate_list_of_events_from_page(tippmix_page)
all_events.extend(events)

for event in all_events:
    event.print_event()

browser.close()
