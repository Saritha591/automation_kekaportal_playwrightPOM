from libs.kekaportal import Kekaportal_LoginPage
from playwright.sync_api import Playwright, sync_playwright
from data import config

username = config.username
password = config.password


def test_goto_url(page):
    portal = Kekaportal_LoginPage(page)
    portal.goto()
    portal.kekaportalbtn()

    

