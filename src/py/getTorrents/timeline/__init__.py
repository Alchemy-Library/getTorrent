import time

from browser.Chrome import openPage
from profile.account.my import user
from movement import scrollDown

home = f"https://twitter.com/{user}"
replies = f"{home}/with_replies"
media = f"{home}/media"
likes = f"{home}/likes"


def toTimeline(section, scroll=False):
    openPage(section)
    time.sleep(3)
    if scroll:
        scrollDown()
    print("Opened Home")
