import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManagerfrom selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.accept()

time.sleep(3)

BUTTON_3 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
time.sleep(3)
print(alert.text)

alert.dismiss()

time.sleep(3)

