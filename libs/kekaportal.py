from data import config


class Kekaportal_LoginPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.kekaportal = page.locator(
            "//p[normalize-space()='Keka Password']")
        self.username = page.locator("//input[@id='email']")
        self.password = page.locator("//input[@id='password']")
        self.loginbtn = page.locator("//button[normalize-space()='Login']")
        self.homepage = page.locator(
            "//span[@class='ic-home sidebar-list-icon']")
        self.homepage_gotoBirthdays = page.locator(
            "//span[@class='icon ic-cake icon-xxs icon-accent-red']")
        self.MetabPage = page.locator(
            "//span[@class='ic-person sidebar-list-icon']")
        self.attendence_tab = page.locator(
            "//span[normalize-space()='Attendance']")
        self.inboxtab = page.locator(
            "//span[@class='ic-inbox sidebar-list-icon']")
        self.inboxtab_action = page.locator("a[routerlink='action']")
        self.Take_action = page.locator(
            "//span[@class='ic-rupee sidebar-list-icon']")
        self.teamtab = page.locator("//li[@class='nav-item active']")
        self.org = page.locator(
            "//li[@class='nav-item active']//a[@class='nav-link']")
        self.org_emp = page.locator("//span[normalize-space()='Employees']")
        self.screenshot = page.screenshot(
            path="screenshot1.png,full_page=True")
        self.control_1 = page.keyboard.press
        self.control_2 = page.keyboard.press
        self.control_3 = page.keyboard.press
        self.mousewheel = page.mouse.wheel(0, 800)

    def goto(self):
        self.page.goto("https://msys.keka.com/")

    def kekaportalbtn(self):
        self.kekaportal.click()

    def login_details(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginbtn.click()

    def home_Pagelocator(self):
        self.homepage.click()
        self.homepage_gotoBirthdays.click()

    def attendence(self):
        self.MetabPage.click()
        self.attendence_tab.click()

    def TakeAction_inbox(self):
        self.inboxtab.click()
        self.Take_action.click()

    def Myteam_page(self):
        self.teamtab.mouse.wheel(0, 800)

    def Org_Employees(self):
        self.org.click()
        self.org_emp.press("Enter")
