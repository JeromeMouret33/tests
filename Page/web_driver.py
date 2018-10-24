from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class WebDriver(object):
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument("--lang=en-us")
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        self.downloads = r"C:\tmp\reports"
        self.chrome_options.add_experimental_option("prefs", {
        "download.default_directory": self.downloads,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 120)

    def get_driver(self):
        return self.driver

    def set_download_default_directory(self, directory):
        self.downloads = directory
