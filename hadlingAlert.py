from selenium import webdriver
import time
drive= webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')

drive.get("https://testautomationpractice.blogspot.com/")

drive.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(3)

#drive.switch_to.alert.accept()

drive.switch_to.alert.dismiss()