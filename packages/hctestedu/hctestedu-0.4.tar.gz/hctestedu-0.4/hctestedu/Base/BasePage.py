from selenium import webdriver


class BasePage(object):
    def __init__(self, browser):
        # driver_path = r"D:\driver\95ver\chromedriver.exe"
        # self.driver = webdriver.Chrome(executable_path=driver_path)
        self.browser = browser

        # 打开网站

    def get_url(self, url):
        self.browser.get(url)
        # 关闭浏览器

    def quit_browser(self):
        self.browser.quit()

    # # 输入字符
    def send_keys(self, selector, context):
        self.browser.find_element(*selector).send_keys(context)

    # 点击
    def click(self, selector):
        self.browser.find_element(*selector).click()
