from selenium import webdriver
#from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import 
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
print("hii")