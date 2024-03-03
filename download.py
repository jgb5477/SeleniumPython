import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
'''
chromeOption = Options()
chromeOption.add_experimental_option("pref",{"download.default_directory": "/Users/deepintent/Downloads"})
'''
myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')#,chrome_options=chromeOption)
myweb.get("http://demo.automationtesting.in/FileDownload.html")

time.sleep(2)
myweb.find_element(By.ID, "textbox").send_keys("Testing the element")
time.sleep(3)
myweb.find_element(By.ID,"createTxt").click()
time.sleep(2)
myweb.find_element(By.ID,"link-to-download").click()


