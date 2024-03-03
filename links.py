from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#print(myweb.title)
assert "Selenium Practice Form" in myweb.title

links= myweb.find_elements(By.TAG_NAME,"a")

print(f"Number of Links on page: {len(links)}")

for l in links:
    print(l.text)

#myweb.find_element(By.LINK_TEXT,"Software Testing Tutorials").click()

myweb.find_element(By.PARTIAL_LINK_TEXT,"Sof").click()