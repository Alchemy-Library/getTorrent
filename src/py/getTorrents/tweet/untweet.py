import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser.Chrome import driver

delay = 0.3


def dropdownMenu(tweet):
    try:
        tweet.click()
    except:
        print("Failed Click! Untweet")
        return -1

    time.sleep(0.1)
    return driver.find_element(By.XPATH, "//div[@data-testid='Dropdown']")


def deleteTweet(t):
    dropdown = dropdownMenu(t)
    if dropdown == -1:
        return -1

    time.sleep(0.1)
    button = dropdown.find_elements(By.XPATH, "//div[@role='menuitem']")
    delete = button[0]
    delete.send_keys(Keys.RETURN)

    return confirmDelete()


def confirmDelete():
    delete = driver.find_elements(By.XPATH, "//div[@data-testid='confirmationSheetConfirm']")
    time.sleep(0.1)
    if len(delete) > 0:
        delete[0].click()
        return -1
    else:
        return 0
    print(f"Deleted")


def findTweet():
    tweet = driver.find_elements(By.XPATH, "//div[@data-testid='caret'][@aria-haspopup='menu']")
    return tweet


def deleteTweets():
    t = findTweet()[0]
    rc = deleteTweet(t)
    time.sleep(delay)
    return rc


'''# alt
tweet = findTweets()
i = 0
while len(tweet):
    deleteTweet(tweet[i])
    i = i + 1
'''
