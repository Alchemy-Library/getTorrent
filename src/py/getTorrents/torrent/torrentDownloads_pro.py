import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def openPage(page, sleep=3):
    driver.get(page)
    time.sleep(sleep)


def getRow():
    skip = 6
    rows = driver.find_elements(By.CLASS_NAME, "grey_bar3")
    return rows[skip: -1]
    return rows


def searchTorrents():
    sch = "https://www.torrentdownloads.pro/search/?search=kotlin+android"
    openPage(sch, 3)

    torrent = []
    for i, v in enumerate(getRow()):
        a = v.find_elements(By.TAG_NAME, "a")
        torrent.append(a[0].get_attribute('href'))
    return torrent


def openTorrentPage(pages):
    for i in pages:
        openPage(i, 2)
        print(f"{i} opened")
        if i > 5:
            break


pages = searchTorrents()
print("Hello")
print(pages)