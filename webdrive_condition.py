from selenium import webdriver
import time
import selenium.webdriver.common.by as By

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://app.bamboohr.com/login/")
print(myweb.title)
user_el = myweb.find_element(By.NAME,"username")
print(user_el.is_displayed())
print(user_el.is_enabled())

user_el.send_keys("deepintent")
myweb.find_element_by_id("submit").click()

user_ele=myweb.find_element_by_id("lemail")
print(user_ele.is_displayed())
print(user_ele.is_enabled())
pass_ele=myweb.find_element_by_name("password")
print(pass_ele.is_enabled())
print(pass_ele.is_displayed())
time.sleep(5)
user_ele.send_keys("jayesh.bangad@deepintent.com")
pass_ele.send_keys("Jayesh1234")

myweb.find_element_by_css_selector("button[type=submit]").click()

myweb.find_element_by_class_name("jss-a41").click()






