import time
from selenium import webdriver

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://www.amazon.in/")

cookies = myweb.get_cookies()
print(len(cookies))

print(cookies)

cookie = {'name': 'Mycookie', 'value': '1234567890'}
myweb.add_cookie(cookie)

cookies = myweb.get_cookies()
print(len(cookies))

print(cookies)

myweb.delete_cookie('Mycookie')
time.sleep(3)
cookies = myweb.get_cookies()
print(len(cookies))
print(cookies)

myweb.delete_all_cookies()
time.sleep(3)
cookies = myweb.get_cookies()
print(len(cookies))