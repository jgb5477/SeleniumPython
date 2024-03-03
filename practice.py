'''

from selenium import webdriver

myweb= webdriver.Chrome()
myweb.get("https://www.google.com/")
print(myweb.title)
print(myweb.current_url)


from selenium import webdriver
from selenium.webdriver.common.by import By
myweb = webdriver.Chrome()
myweb.get('https://demo.guru99.com/test/newtours/')

myweb.find_element(By.NAME,"userName").send_keys("Mercury")
myweb.find_element(By.NAME,"password").send_keys("Mercury")
myweb.find_element(By.NAME,"submit").click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
myweb = webdriver.Chrome()
myweb.get("https://testautomationpractice.blogspot.com/")

ele = myweb.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
action =ActionChains(myweb)
action.double_click(ele).perform()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

myweb = webdriver.Chrome()
myweb.get("https://testautomationpractice.blogspot.com/")

source = myweb.find_element(By.ID,"draggable")
destination = myweb.find_element(By.ID,"droppable")

action = ActionChains(myweb)

action.drag_and_drop(source,destination).perform()


from selenium import webdriver
from selenium.webdriver.common.by import By
myweb = webdriver.Chrome()
myweb.get("https://testautomationpractice.blogspot.com/")

myweb.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()

myweb.switch_to.alert.accept()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

myweb = webdriver.Chrome()
myweb.get('https://testautomationpractice.blogspot.com/')

ele = myweb.find_element(By.ID,"speed")
drp = Select(ele)

drp.select_by_visible_text("Fast")



from selenium import webdriver
from selenium.webdriver.common.by import By

myweb = webdriver.Chrome()
myweb.get("https://testautomationpractice.blogspot.com/")

myweb.maximize_window()

myweb.execute_script("window.scrollBy(0,1000)","")



import time
from selenium import webdriver

myweb = webdriver.Chrome()
myweb.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
myweb.get("https://www.google.com/")
time.sleep(3)
myweb.back()
time.sleep(3)
myweb.forward()
time.sleep(3)
myweb.close()
'''

