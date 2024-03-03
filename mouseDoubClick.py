import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)
element=myweb.find_element(By.XPATH,"//*[@id='sidebar-right-1']//button")

action=ActionChains(myweb)
action.double_click(element).perform()
