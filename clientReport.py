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
    print 'Entering Username'
    # Find The PassWord Field and Enter Password
    driver.find_element_by_id('user-password').send_keys(password)
    print 'Entering Password'
    # Find The Sign In Button and Click It Which Will Log Us In
    driver.find_element_by_id('sign-in-button').click()
    print 'Clicking Signin Button'
    # Wait For Ten Seconds
    print 'Waiting 30 Seconds For Page To Load'
    time.sleep(30)
    # Find The Icon To Take You To The Website Selection and Click It
    driver.find_element_by_class_name('icon-websites2').click()
    print 'Click The Dasboard Icon'
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
    print 'Hovering Over The Correct Site and Then Clicking The Dasboard Icon'
    time.sleep(2)
    # Click On The Dash Board Icon
    mainDiv.find_element_by_class_name('fa-dashboard').click()
    # Click On The Client Report Button
    driver.find_element_by_id('sidebar-tool-client-report').click()
    print 'Clicking The Client Report Button'
    # Wait Two Seconds
    print 'Waiting Two Seconds...'
    time.sleep(2)
    # Click On The New Report Button
    driver.find_element_by_xpath(
        '//div[@analytics-event="Go To New Report"]').click()
    print 'Clicking The New Report Button'
    print 'Waiting Two Seconds'
    time.sleep(2)
    # Click On The Select Box
    driver.find_element_by_id('client-report-template').click()
    print 'Clicking On The Select Box'
    # Click On The Template Name
    driver.find_element_by_xpath(
        '//option[@label="Monthly Website Care Plan"]').click()
    print 'Choosing The Correct Template'
    # Click On The Select Box Again
    driver.find_element_by_id('client-report-template').click()
    print 'Clicking Off The Select Box'
    # Wait On Second
    print 'Waiting One Second...'
    time.sleep(1)
    # Click The Accept Cookies Button
    driver.find_element_by_class_name('success').click()
    print 'Click The Accept Cookies Button'
    # Wait One Second
    print 'Waiting Two Seconds.....'
    time.sleep(1)
    # Click On The Customize Button
    driver.find_element_by_class_name('btn-arrows').click()
    print 'Click The Customize Button'
    # Wait One Second
    print 'Waiting Two Seconds....'
    time.sleep(2)
    # Click On the Preview And Download Button
    driver.find_element_by_xpath(
        '//button[@ng-click="createReport()"]').click()
    print 'Click The Preview and Download Button'
    # Wait 20 Seconds For The Report To Be Generated
    print 'Wait One Minute For It To Generate'
    time.sleep(60)
    # Click The Download As PDF Button
    driver.find_element_by_class_name('fa-file-pdf').click()
    print 'Clicking The Download As PDF Button'
    # Wait Ten Seconds
    print 'Wait Ten Seconds For It To Download'
    time.sleep(10)
    # Close The Browser
    driver.quit()
