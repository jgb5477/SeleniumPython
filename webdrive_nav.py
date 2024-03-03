from selenium import webdriver
import time
myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("http://demo.automationtesting.in/Windows.html")
print(myweb.title)
myweb.get("https://www.geeksforgeeks.org/")
print(myweb.title)
time.sleep(3)
myweb.back()
print(myweb.title)
time.sleep(3)
myweb.forward()
print(myweb.title)
time.sleep(3)

myweb.close()