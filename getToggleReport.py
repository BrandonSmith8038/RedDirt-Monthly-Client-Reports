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


def getToggleReport(ID):
    print(ID)
    # Toggl UserName
    userName = TOGGL_USERNAME
    # Toggl Password
    password = TOGGL_PASSWORD
    # Url To Browse To
    url = 'https://toggl.com/login/'
    # Load The Chrome WebDriver
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    # Browse To The Site
    driver.get(url)
    # Wait Two Seconds
    time.sleep(2)
    # Enter UserName Into Form
    print 'Entering Username'
    driver.find_element_by_id('login-email').send_keys(userName)
    # Enter Password Into Form
    print 'Entering Password'
    driver.find_element_by_id('login-password').send_keys(password)
    # Click The Login Button
    print 'Clicking The Login Button'
    driver.find_element_by_id('login-button').click()
    # Sleep For 10 Seconds
    print 'Wait 10 Seconds For The Page To Load'
    time.sleep(10)
    # Click The Reports Button
    print 'Click The Reports Button'
    driver.find_element_by_class_name('css-s4ncty').click()
    # Switch The Time To Last Month
    # Click The Drop Down
    print 'Click The Dropdown'
    driver.find_element_by_class_name('period-popdown-controls ').click()
    # Click The Last Month Button
    print 'Click The Last Month Button'
    driver.find_element_by_xpath(
        '//a[@data-name="prevMonth"]').click()
    # Click The Project Button
    print 'Click The Project Button'
    driver.find_element_by_class_name('for-reportprojects').click()
    # Wait One Second
    print 'Wait 2 Seconds'
    time.sleep(2)
    # Click The Client We Are Looking For
    # Find The Correct Client
    print 'Click On The Correct Client'
    idToFind = '//label[@for="project-checkbox-{}-id"]'.format(ID)
    driver.find_element_by_xpath(idToFind).click()
    # Wait One Second
    print ('Waiting 2 Seconds...')
    time.sleep(2)
    # Click Off The Drop Down
    print 'Clicking Off The Dropw Down With The Return Key'
    clickEsc = ActionChains(driver).send_keys(Keys.RETURN)
    clickEsc.perform()
    # Wait Two Seconds
    print 'Waiting 2 Seconds....'
    time.sleep(2)
    # Click The Apply Button
    print 'Clicking The Apply Button'
    driver.find_element_by_class_name('btn-filter-container').click()
    # Wait 3 Seconds
    print 'Waiting 3 Seconds....'
    time.sleep(3)
    # Click The Plus Icon
    # If There Is No Total Just Exit
    print 'Checking If There Are Any Time Entries, If There Is Not Exit'
    try:
        driver.find_element_by_class_name('col-total').click()
    except NoSuchElementException:
        return
    # Wait Two Seconds
    print 'Waiting 2 Seconds....'
    time.sleep(2)
    # Click The Export Dropdown
    print 'Click on The Export Button'
    driver.find_element_by_class_name('export-box').click()
    # Click The Export As PDF Button
    print 'Click On The PDF Button'
    driver.find_element_by_xpath('//a[@data-value="pdf"]').click()
    print 'Waiting 5 Seconds'
    # Wait 5 Seconds
    time.sleep(5)
    driver.quit()
