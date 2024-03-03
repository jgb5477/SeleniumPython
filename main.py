from selenium import webdriver
import time
myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("http://demo.automationtesting.in/Windows.html")
print(myweb.title)
print(myweb.current_url)
#print(myweb.page_source) #return HTML code of the Page
myweb.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)
#myweb.close() # closes current browser
myweb.quit() # closes all tabs