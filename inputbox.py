from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

num=myweb.find_elements(By.CLASS_NAME,'text_field')
print(len(num))

status=myweb.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print(f"Displayed or not: {status}")
status=myweb.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print(f"Enabled or not: {status}")

myweb.find_element(By.ID,'RESULT_TextField-1').send_keys('Jayesh')
myweb.find_element(By.ID,'RESULT_TextField-2').send_keys('Bangad')
myweb.find_element(By.ID,'RESULT_TextField-3').send_keys('9768543223')
