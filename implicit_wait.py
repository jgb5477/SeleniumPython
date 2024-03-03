from selenium import webdriver

drive= webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')

drive.get("https://www.geeksforgeeks.org/")
drive.find_element_by_class_name('gcse-search__btn').click()
drive.implicitly_wait(10)
drive.find_element_by_class_name('gcse-search-input__wrapper').send_keys('Arrays')

