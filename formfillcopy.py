# to read data from excel we install xlrd from pip then import sheet
from os import name
from telnetlib import EC
from xlrd import sheet
import xlrd
#read excel sheet row column etc.
workbook1 = xlrd.open_workbook("testsheets.xls")
sheet2 = workbook1.sheet_by_name("S2")
row_count2 = sheet2.nrows
col_count2 = sheet2.ncols
#SELENIUM PROGRAMING
from selenium import webdriver
from selenium.webdriver.common.by import By
#for using actionclass import these
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
#for explicit wait import these
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path= "C:\\BIkash Practice\\Python\\Python38-32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.orangehrm.com/contact-sales/")

"""#Row are zero indexing , but first row conating Header Name reading only name colume so 1st column
for row in range(1,row_count2):
        # 0 th Column name is Name 
        col_name = sheet2.cell_value( row , 0)
        print(col_name)       
        driver.find_element_by_id("Form_submitForm_FullName").send_keys(col_name)
        print("--")
        driver.implicitly_wait(10)

#start reading data of a single person so read 1st row
for col in range(0 , col_count2):
    #read data of 1st row
    person1_data = sheet2.cell_value(1 , col)
    print (person1_data)"""

#reading value from excel individually 
name = sheet2.cell_value( 1 , 0)
comp_name = sheet2.cell_value( 1 , 1)
job_title = sheet2.cell_value( 1 , 2)
cont_mob = sheet2.cell_value(1 , 3)
email_id = sheet2.cell_value (1 , 4)
message_comment = sheet2.cell_value( 1 , 5)
"""driver.find_element_by_id("Form_submitForm_FullName").send_keys(name)
driver.find_element_by_id("Form_submitForm_CompanyName").send_keys(comp_name)
driver.find_element_by_id("Form_submitForm_JobTitle").send_keys(job_title)
driver.find_element_by_id("Form_submitForm_Contact").send_keys(cont_mob)
driver.find_element_by_id("Form_submitForm_Email").send_keys(email_id)
driver.find_element_by_id("Form_submitForm_Comment").send_keys(message_comment)
e = Select(driver.find_element_by_id("Form_submitForm_NoOfEmployees"))
e.select_by_visible_text("51 - 75")"""

#reading value from excel individually using explicit wait
w = WebDriverWait(driver, 10)
fullname = w.until(EC.visibility_of_element_located((By.ID,'Form_submitForm_FullName')))
fullname.send_keys(name)
compname = w.until(EC.visibility_of_element_located((By.ID,'Form_submitForm_CompanyName')))
compname.send_keys(comp_name)
jobtitle = w.until(EC.visibility_of_element_located(BY.ID(())))

#driver.get("https://www.orangehrm.com/")

#a= ActionChains(driver)
#m = driver.find_element_by_class_name("link")
#a.move_to_element(m).perform()
#driver.maximize_window()
#driver.implicitly_wait(3)
#driver.get("https://www.orangehrm.com/contact-sales/")

"""e = Select(driver.find_element_by_id("Form_submitForm_NoOfEmployees"))
e.select_by_visible_text("51 - 75")
n = driver.find_element_by_link_text("FREE TRIAL")
driver.implicitly_wait(3)
driver.find_element_by_id("Form_submitForm_Contact").send_keys("9373198954")
driver.implicitly_wait(3)
driver.find_element_by_id("Form_submitForm_Email").send_keys("patel.deepti16@gmail.com")
driver.implicitly_wait(3)
driver.find_element_by_id("Form_submitForm_Comment").send_keys("patel.deepti16@gmail.com")

n = driver.find_elements_by_css_selector("#header-navbar > ul.nav.navbar-nav.navbar-right.extended-nav > li:nth-child(1) > a")
a.move_to_element(n).click()"""

time.sleep(10)
driver.quit()