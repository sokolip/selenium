c

driver.get("https://freeconferencecall.com/global/pl")

login_button = driver.find_element("xpath", "//a[@id = 'login-desktop']")
login_button.click()

email_field = driver.find_element("xpath", '//input[@id = "login_email"]')
email_field.send_keys("simple@ya.ru")
email_field.clear()

print(email_field.get_attribute("value"))


time.sleep(3)