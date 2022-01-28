from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
#driver.get("https://www.google.com/")
#driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys("software testing")
#driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div.SDkEP > div.a4bIc > input").send_keys("hello")
#driver.find_element (By.ID , 'input') . send_keys ("software testing")

#driver.find_element (By.CLASS_NAME , 'gLFyf gsfi') . send_keys ("software testing")
#driver.find_element(By.NAME, 'q').send_keys("Software testing")
#driver.get("https://www.amazon.com")
#driver.find_element_by_id("twotabsearchtextbox").send_keys("toys")

#driver.get("https://www.youtube.com/")
#driver.find_element (By.ID , 'search') . send_keys("songs")
#driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input/id").send_keys("songs")
driver.get("https://www.orangehrm.com/")
driver.find_element (By.ID , 'myText').send_keys ("patel.deepti16@gmail.com")

print(driver.title)
driver.quit()

