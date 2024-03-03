import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

time.sleep(3)
element=myweb.find_element(By.XPATH,"//*[@class='document']/p/span")

action=ActionChains(myweb)
action.context_click(element).perform()

myweb.find_element(By.XPATH,"//*[@class='context-menu-list context-menu-root']/li[2]").click()