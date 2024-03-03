import time
from selenium import webdriver

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://www.amazon.in/")

#myweb.save_screenshot("/Users/deepintent/Downloads/home.png")

myweb.get_screenshot_as_file("/Users/deepintent/Downloads/home2.png")