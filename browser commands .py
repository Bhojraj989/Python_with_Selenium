import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://www.simplyhired.co.in/search?q=workday&l=india&job=ESvGHTNSApM1tSohV35k39HDmo0JScN4MVKLQZo4SB1icxHz7jqusg")
time.sleep(4)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)
driver.find_element(By.XPATH,"https://practice.expandtesting.com/checkboxes#:~:text=Playwright%2C%20Cypress%2C%20etc.-,Checkbox%201,-Checkbox%202").click()
# driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
# forgot_password.click()
driver.back()

