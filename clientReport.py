#!/usr/bin/env python
from selenium import webdriver
# Bring In Actions To Allow To Hover Effect
from selenium.webdriver.common.action_chains import ActionChains
# Grab Hidden Variables
from keys import MANAGE_WP_PASSWORD
from keys import MANAGE_WP_USERNAME
# Import The Time Class
import time


def getClientReport(siteName):
    # URL TO Browse To
    url = 'https://orion.managewp.com/login'
    # Orion UserName
    userName = MANAGE_WP_USERNAME
    # Orion Password
    password = MANAGE_WP_PASSWORD
    # Load The Chrome WebDriver
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    # Browse To The Orion Site
    driver.get(url)
    # Wait 5 Seconds
    time.sleep(2)
    # Find The UserName Field and Enter UserName
    driver.find_element_by_id('user-email').send_keys(userName)
    # Find The PassWord Field and Enter Password
    driver.find_element_by_id('user-password').send_keys(password)
    # Find The Sign In Button and Click It Which Will Log Us In
    driver.find_element_by_id('sign-in-button').click()
    # Wait For Ten Seconds
    time.sleep(10)
    # Find The Icon To Take You To The Website Selection and Click It
    driver.find_element_by_class_name('icon-websites2').click()
    # Find The Correct Website
    siteName = '//div[@data-test-site-name="{}"]'.format(siteName)
    ######## USE THIS ONE IF GRABBING MULTIPLE SITES #####
    #mainDiv = driver.find_element_by_xpath(siteName)
    ####### USE THIS ONE IF GRABBING A SINGLE SITE #######
    mainDiv = driver.find_element_by_xpath(
        '//div[@data-test-site-name="Justin Sports Medical Team"]')
    # #Hover Over That Div To Reveal The Icons
    hover = ActionChains(driver).move_to_element(mainDiv)
    hover.perform()
    # Wait One Second
    time.sleep(2)
    # Click On The Dash Board Icon
    mainDiv.find_element_by_class_name('fa-dashboard').click()
    # Click On The Client Report Button
    driver.find_element_by_id('sidebar-tool-client-report').click()
    # Wait Two Seconds
    time.sleep(2)
    # Click On The New Report Button
    driver.find_element_by_xpath(
        '//div[@analytics-event="Go To New Report"]').click()
    time.sleep(2)
    # Click On The Select Box
    driver.find_element_by_id('client-report-template').click()
    # Click On The Template Name
    driver.find_element_by_xpath(
        '//option[@label="Monthly Website Care Plan"]').click()
    # Click On The Select Box Again
    driver.find_element_by_id('client-report-template').click()
    # Wait On Second
    time.sleep(1)
    # Click The Accept Cookies Button
    driver.find_element_by_class_name('success').click()
    # Wait One Second
    time.sleep(1)
    # Click On The Customize Button
    driver.find_element_by_class_name('btn-arrows').click()
    # Wait One Second
    time.sleep(2)
    # Click On the Preview And Download Button
    driver.find_element_by_xpath(
        '//button[@ng-click="createReport()"]').click()
    # Wait 20 Seconds For The Report To Be Generated
    time.sleep(20)
    # Click The Download As PDF Button
    driver.find_element_by_class_name('fa-file-pdf').click()
    # Wait Ten Seconds
    time.sleep(10)
    # Close The Browser
    driver.quit()
