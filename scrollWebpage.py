import time
from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

myweb.maximize_window()
time.sleep(3)

#myweb.execute_script("window.scrollBy(0,1000)","")

#flag=myweb.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[72]/td[2]')
#myweb.execute_script("arguments[0].scrollIntoView();",flag)

myweb.execute_script("window.scrollBy(0,document.body.scrollHeight)")