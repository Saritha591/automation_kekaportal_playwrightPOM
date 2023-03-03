from libs.kekaportal import Kekaportal_LoginPage
from playwright.sync_api import Page
from data import config

username = config.username
password = config.password

def test_inboxtab(page):
    portal = Kekaportal_LoginPage(page)
    portal.goto()
    portal.kekaportalbtn()
    portal.login_details(username,password)
    portal.home_Pagelocator()
    portal.attendence()
    portal.TakeAction_inbox()


