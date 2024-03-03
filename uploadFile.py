import time
from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://testautomationpractice.blogspot.com/")


flag="/Users/deepintent/Downloads/IMG_20220531_103914.jpg"
time.sleep(3)
myweb.switch_to.frame(0)
myweb.find_element(By.ID,"RESULT_FileUpload-10").send_keys(flag)
