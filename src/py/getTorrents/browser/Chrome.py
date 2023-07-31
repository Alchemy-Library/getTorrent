import time
from selenium import webdriver

driver = webdriver.Chrome()


def openPage(page, keep=False):
    driver.get(page)
    if keep:
        time.sleep(3600)


def closeChrome():
    driver.quit()
