import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def openPage(page, sleep=1):
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


def countTabs():
    handles = len(driver.window_handles)
    return handles


def newTab(max=99):
    if countTabs() < max:
        driver.switch_to.new_window('tab')


def openTorrentPages(pages):
    newTab(2)
    for i in pages:
        openPage(i, 2)
        print(f"{i} opened")
        if i > 5:
            break


def getDownloadLink():
    download = driver.find_element(By.CLASS_NAME, "download")
    link = download.find_elements(By.TAG_NAME, "a")[1]
    return link.get_attribute('href')


def getDownloadLinks(tors, max=50):
    newTab(2)
    links = []
    for i, tor in enumerate(tors):
        if i > (max - 1):
            break
        openPage(tor, 1)
        links.append(getDownloadLink())
        print(i)
    closeTab()
    return links


def closeTab():
    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    driver.close()
    driver.switch_to.window(parent)


def dlTorrent(l):
    newTab()
    openPage(l)


def downloadTorrents(links):
    for l in links:
        dlTorrent(l)
    for l in links:
        closeTab()
        time.sleep(0.5)


def downloadAll(num):
    tors = searchTorrents()
    links = getDownloadLinks(tors, num)
    downloadTorrents(links)


if __name__ == '__main__':
    downloadAll(50)
