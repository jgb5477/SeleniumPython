import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source = myweb.find_element(By.XPATH,"//*[@id='box6']")
destination = myweb.find_element(By.XPATH,"//*[@id='box106']")

action = ActionChains(myweb)
action.drag_and_drop(source,destination).perform()

