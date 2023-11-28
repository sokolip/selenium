import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")
time.sleep(3)

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

ENABLE_IN_SECONDS = ("xpath", "//button[@id='enableAfter']")
wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS)).click()

driver.get()