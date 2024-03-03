import time

from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

myweb.switch_to.frame("packageListFrame")
myweb.find_element(By.LINK_TEXT,"org.openqa.selenium.bidi").click()
myweb.switch_to.default_content()
time.sleep(3)

myweb.switch_to.frame("packageFrame")
myweb.find_element(By.XPATH,"/html/body/main/div/section[2]/ul/li[2]").click()
myweb.switch_to.default_content()

time.sleep(3)
myweb.switch_to.frame("classFrame")
myweb.find_element(By.CLASS_NAME,"navBarCell1Rev").click()

