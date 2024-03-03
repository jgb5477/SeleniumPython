from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')

myweb.get("file:/Users/deepintent/PycharmProjects/SeleniumPython/sample.html")

rows= len(myweb.find_elements(By.XPATH,"/html/body/table/tbody/tr"))
cols= len(myweb.find_elements(By.XPATH,"/html/body/table/tbody/tr[1]/th"))

print(rows)
print(cols)
print("Products   "+"Articles   "+"Price")
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=myweb.find_element(By.XPATH,"/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='    ')
    print()