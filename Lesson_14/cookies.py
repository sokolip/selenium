import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

#print(driver.get_cookie("country_code"))
driver.get_cookies()

driver.add_cookie({
    "name" : "Example"
    "value" : "123323"
})

print(driver.get_cookie("Example"))

before = driver.get_cookie("split")
print(before)

driver.delete_cookie("split")
driver.add_cookie({
    "name" : "split"
    "value" : "QWERTY"
})

after = driver.get_cookie("split")
print(after)

 
