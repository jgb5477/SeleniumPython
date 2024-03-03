from selenium import webdriver
from selenium.webdriver.common.by import By


myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("http://demo.automationtesting.in/Windows.html")

myweb.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

print(myweb.current_window_handle)

handles= myweb.window_handles

for h in handles:
    myweb.switch_to.window(h)
    print(myweb.title)
    if myweb.title=="Frames & windows":
        myweb.close()

myweb.quit()