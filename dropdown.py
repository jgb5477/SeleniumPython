from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element= myweb.find_element(By.ID,"RESULT_RadioButton-9")
drp= Select(element)

#drp.select_by_visible_text('Afternoon')

#drp.select_by_index(3)

#drp.select_by_value("Radio-2")

print(len(drp.options))

all_opt=drp.options

for o in all_opt:
    print(o.text)
