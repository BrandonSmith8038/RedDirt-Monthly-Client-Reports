#!/usr/bin/env python
from selenium import webdriver
# Bring In Actions To Allow To Hover Effect
# Bring In Actions To Allow To Press ESC Key
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# Grab Hidden Variables
from keys import TOGGL_USERNAME
from keys import TOGGL_PASSWORD
# Import The Time Class
import time


def getAnalyticReport(siteName):
    print('Analytics Report')
