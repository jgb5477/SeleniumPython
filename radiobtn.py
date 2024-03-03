from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

status=myweb.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected()
print(f"Male is selected or not: {status}")

