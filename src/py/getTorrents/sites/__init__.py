from browser.Chrome import driver, openPage
from url import URL

site = ["https://www.torrentdownloads.pro", "https://torrentgalaxy.to", "https://thepiratebay.org"]


class Search():
    def __int__(self, kwd):
        self.kwd = kwd
        self.search = self.get(kwd)

    def get(self, kwd, index=-1):
        self.search = [
            f"https://www.torrentdownloads.pro/search/?search={URL.format(kwd)}",
            f"https://torrentgalaxy.to/torrents.php?search={URL.format(kwd)}",
            f"https://thepiratebay.org/search.php?q={URL.format(kwd)}&all=on&search=Pirate+Search&page=0&orderby="
        ]
        if index >= 0:
            return self.search[index]
        else:
            return self.search

    def open(self):
        for s in self.search:
            openPage(s)


def tests(kwd="android studio"):
    search = Search(kwd)
    print(search.search)
