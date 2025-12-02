import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username_text = "standard_user"
password_text = "secret_sauce"
##username = driver.find_element(By.ID,"user-name")
##password = driver.find_element(By.ID,"password")
username = driver.find_element(By.NAME,"user-name")
password = driver.find_element(By.NAME,"password")


username.send_keys(username_text)
password.send_keys(password_text)

login_button = driver.find_element(By.ID,"login-button")
login_button.click()

driver.implicitly_wait(2)

title = driver.find_element(By.CLASS_NAME,"title")
assert title.text == "Products"

burger_menu = driver.find_element(By.ID,"react-burger-menu-btn")
burger_menu.click()

side_bar = driver.find_element(By.ID,"inventory_sidebar_link")
side_bar.click()

side_bar_close = driver.find_element(By.ID,"react-burger-cross-btn")
side_bar_close.click()

add_to_cart = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
add_to_cart.click()

driver.implicitly_wait(2)

cart_class = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
cart_class.click()
driver.implicitly_wait(2)

checkout_button = driver.find_element(By.ID,"checkout")
checkout_button.click()

first_name = driver.find_element(By.ID,"first-name")
last_name = driver.find_element(By.ID,"last-name")
zip_code = driver.find_element(By.ID,"postal-code")

first_name.send_keys("Bhoj")
last_name.send_keys("Raj")
zip_code.send_keys("110001")

continue_button = driver.find_element(By.ID,"continue")
continue_button.click()

finish_button = driver.find_element(By.ID,"finish")
finish_button.click()

header_text = driver.find_element(By.CLASS_NAME,"complete-header").text
complete_text = driver.find_element(By.CLASS_NAME,"complete-text").text

act_header_text = "Thank you for your order!"
act_complete_text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

try:
    assert  act_header_text == header_text, "assertion failed"
except AssertionError as e:
    print("Assertion error appear : ", e)
try:
    assert  act_complete_text == complete_text, "IInd assertion failed"
except AssertionError as e:
    print("Assertion error appear : ", e)

print("order is placed successfully!!")
driver.implicitly_wait(2)

driver.quit()