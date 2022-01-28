from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#rom webdriver_manager.Chrome import chromedrivermanager
driver = webdriver.Chrome(executable_path = "C:\\BIkash Practice\\Python\\Python38-32\\chromedriver.exe")

#driver = webdriver.Chrome (chromedrivermanager().install())

#driver.get("https://www.google.com/")
#driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys("gbgdff")

#driver.get("https://www.amazon.com/")
#driver.find_element_by_id("nav-link-accountList-nav-line-1") . click()
#driver.find_element (By.ID , 'nav-link-accountList-nav-line-1') . click()
#driver.find_element (By.ID , 'ap_email') . send_keys("9373198954")
#driver.find_element (By.ID , 'continue') . click()

driver.get("https://www.youtube.com/")
driver.find_element(By.ID , 'search') . send_keys("songs")
driver.find_element_by_id("button") . click()
#driver.implicitly_wait(10)
print(driver.title)
print("hii")
driver.quit()

