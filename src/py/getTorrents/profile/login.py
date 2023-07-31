import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser.Chrome import driver, openPage
from profile.account.my import *


def enter(ele, tab_times=1):
    for i in range(tab_times):
        ele.send_keys(Keys.TAB)
    ele.send_keys(Keys.RETURN)
    time.sleep(0.5)


def getInput():
    return driver.find_element(By.TAG_NAME, "input")


def getInputs():
    '''Return every field with "<input"'''
    return driver.find_elements(By.TAG_NAME, "input")


def login():
    page = "https://twitter.com/i/flow/login?redirect_after_login=%2F"
    openPage(page)
    time.sleep(0.5)
    # Email
    ele = getInput()
    ele.send_keys(email)
    enter(ele)
    # User
    ele = getInput()
    ele.send_keys(user)
    enter(ele)
    # Pass
    ele = getInputs()[1]
    ele.send_keys(password)
    enter(ele, 3)
    # Logged in
    time.sleep(0.5)
