from webdriver_manager import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#browser testing for chrome
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#browser testing for firefox
#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())



#if we have already install driver , no need to install again and again , we can use address for local device 
driver = webdriver.Chrome(executable_path="C://BIkash Practice//Python//chromedriver_win32//chromedriver.exe")

#driver = webdriver.Firefox(executable_path="C:\BIkash Practice\Python\geckodriver-v0.30.0-win64\geckodriver.exe")


driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.implicitly_wait(10)
print(driver.title)
driver.sleep(10)
driver.quit()