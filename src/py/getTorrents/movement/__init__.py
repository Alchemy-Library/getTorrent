from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser.Chrome import driver


def scrollDown():
    '''https://www.programcreek.com/python/example/114687/selenium.webdriver.common.keys.Keys.PAGE_DOWN'''
    element = driver.find_element(By.TAG_NAME, "body")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

