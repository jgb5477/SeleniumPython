import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
myweb.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

Username=myweb.find_element(By.ID,"txtUsername")
Username.click()
Username.send_keys('Admin')
time.sleep(3)

Password=myweb.find_element(By.ID,"txtPassword")
Password.click()
Password.send_keys("admin123")

myweb.find_element(By.ID,"btnLogin").click()
time.sleep(3)

admin = myweb.find_element(By.ID,"menu_admin_viewAdminModule")
userMana = myweb.find_element(By.ID,"menu_admin_UserManagement")
users = myweb.find_element(By.ID,"menu_admin_viewSystemUsers")

time.sleep(3)
actions = ActionChains(myweb)

actions.move_to_element(admin).move_to_element(userMana).move_to_element(users).click().perform()