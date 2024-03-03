import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By

path = "/Users/deepintent/Downloads/login1.xlsx"

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')#,chrome_options=chromeOption)
myweb.get("https://demo.guru99.com/test/newtours/")

row= XLUtils.getRowCount(path,'Sheet1')

for r in range(2,row+1):
    username = XLUtils.readData(path,'Sheet1',r,1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)

    myweb.find_element(By.NAME,"userName").send_keys(username)
    myweb.find_element(By.NAME,"password").send_keys(password)

    myweb.find_element(By.NAME,"submit").click()

    if myweb.title == "Login: Mercury Tours" :
        print("Test Passed")
        XLUtils.writeData(path,'Sheet1', r, 3, "Test Passed")
    else:
        print("Test Failed")
        XLUtils.writeData(path, 'Sheet1', r, 3, "Test Failed")

    myweb.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()
