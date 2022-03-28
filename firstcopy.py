from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\BIkash Practice\\Python\\chromedriver98\\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(5)
driver.minimize_window()
#driver.quit()