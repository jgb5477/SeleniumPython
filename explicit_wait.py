from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://www.indianeagle.com/international-flight-tickets/")


myweb.find_element(By.ID, 'destinationDiv').clear()
myweb.find_element_by_id('destinationDiv').send_keys('DQO')
time.sleep(2)
myweb.find_element_by_xpath('//span[contains(@class,"tt-suggestion")]//div').click()

myweb.find_element_by_id('departureDate').click()
myweb.find_element_by_id('ui-datepicker-div').click()
myweb.find_element_by_id('returnDate').click()

myweb.find_element_by_id('searchFlights').click()

wait = WebDriverWait(myweb,5)
element=wait.until(ec.element_to_be_clickable((By.XPATH,'//div[contains(@class,"panel")]//label[3]')))
element.click()
time.sleep(5)
myweb.quit()

