import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = options()
options.add_argument("--window-size=1920.1080")
options.add_argument("--disable-blink-features=AutomationControlled")


service = Service(ChromeDriverManager().install())
driver = webdriver.chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("")