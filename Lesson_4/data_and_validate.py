import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://www.wikipedia.org")

url = driver.current_url
print("URL страницы:", url)
assert url == "http://www.wikipedia.org", "Ошибка в URL, открыта не та страница"

current_title = driver.title
print("Текущий заголовок:", current_title)
assert current_title == "Wikipedia", "Ошибка в Title, открыта не та страница"

time.sleep(3)
