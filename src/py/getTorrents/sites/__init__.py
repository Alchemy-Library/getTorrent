import time

from browser.Chrome import driver, openPage
from url import URL

site = ["https://www.torrentdownloads.pro", "https://torrentgalaxy.to", "https://thepiratebay.org"]


class Search():
    def __init__(self, kwd):
        self.kwd = kwd
        self.search = self.get()
        self.i = 0

    def get(self, index=-1):
        self.search = [
            f"https://www.torrentdownloads.pro/search/?search={URL.format(self.kwd)}",
            f"https://torrentgalaxy.to/torrents.php?search={URL.format(self.kwd)}",
            f"https://thepiratebay.org/search.php?q={URL.format(self.kwd)}&all=on&search=Pirate+Search&page=0&orderby="
        ]
        if index >= 0:
            return self.search[index]
        else:
            return self.search

    def open(self):
        for s in self.search:
            openPage(s)

    def openIter(self):
        if self.i > len(self.search):
            self.i = 0
        openPage(self.search[self.i])
        self.i += 1

def tests(kwd="kotlin android"):
    search = Search(kwd)
    print(search.search)
    search.openIter()
    time.sleep(1800)

if __name__ == '__main__':
    kwd = "kotlin android"
    tests(kwd)