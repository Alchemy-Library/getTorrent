import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser.Chrome import driver


def confirm():
    '''# Attribute of interest: <div role="menuitem" data-testid="unretweetConfirm">'''
    confirm = driver.find_element(By.XPATH, "//div[@data-testid='unretweetConfirm']")
    confirm.send_keys(Keys.RETURN)
    time.sleep(1)


def unRetweet():
    '''
    Deletes one full page of tweets!
    # Attributes of interest: <div aria-expanded="false" aria-haspopup="menu" role="button" data-testid="unretweet">
    '''
    retweet = driver.find_elements(By.XPATH, "//div[@data-testid='unretweet']")

    for rt in retweet:
        try:
            rt.click()
        except:
            print("Failed Click! UnRetweet")
            return -1
        time.sleep(0.300)
        confirm()
    print("Deleted Retweets")
    return len(retweet)


def deleteRetweets():
    '''Todo: Fix this! return code is sloppy'''
    found = 1
    while found > 0:
        found = unRetweet()
        if found == -1:
            break
    return found
