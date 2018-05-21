#!/usr/bin/env python
from selenium import webdriver
# Bring In Actions To Allow To Hover Effect
from selenium.webdriver.common.action_chains import ActionChains
# Grab Hidden Variables
from keys import MANAGE_WP_PASSWORD
from keys import MANAGE_WP_USERNAME

import time


def createInvoice():
