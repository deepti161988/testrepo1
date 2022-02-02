from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#browser testing for chrome
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#browser testing for firefox
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.youtube.com/watch?v=qmZRPMr8RsI")
print(driver.title)
driver.quit()