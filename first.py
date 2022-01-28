 
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
driver = webdriver.Chrome(executable_path="C://BIkash Practice//Python//chromedriver_win32.exe")
driver.implicitly_wait(5)
#driver.get("https://www.calculator.net/")
driver.get("https://www.google.co.in/")

print("deepti")

def sum( a , b ):
    c = a + b
    return c
d = sum(2,3)
print(d)
print("hello")
driver.quit()