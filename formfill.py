# to read data from excel we have to install xlrd from pip then import sheet
from xlrd import sheet
import xlrd
workbook1 = xlrd.open_workbook("testsheets.xls")
"""sheet1 = workbook1.sheet_by_name("S1")
rowcount1 = sheet1.nrows
colcount1 = sheet1.ncols
print(rowcount1)
print(colcount1)"""
print()
"""result_data = []
for cur_row in range(0 , rowcount):
    row_data = []
    for cur_col in range(0 , colcount):
        data =  sheet1.cell_value(cur_row , cur_col)
        row_data.append(data)
    result_data.append(row_data)
print(result_data)
print(data)"""
#print(cur_row)
#name = sheet1.cell_value( 0 , 0 )
#print(name)
#name1 = sheet1.cell_value( 2 , 2 )
#print(name1)
#workbook1 = xlrd.open_workbook("testsheets.xls")
sheet2 = workbook1.sheet_by_name("S2")
rowcount2 = sheet2.nrows
colcount2 = sheet2.ncols
for rows in range(1,rowcount2):
        name1 = sheet2.cell_value( rows , 0)
        print(name1)
"""name2 = sheet2.cell_value(2,0)
name3 = sheet2.cell_value(3,0)
name4 = sheet2.cell_value(4,0)
print("------")
for cols in range (0 , colcount2):
    data1 = sheet2.cell_value ( 1 , cols)
    print(data1)
print("------")
comname = sheet2.cell_value( 1 , 1)
print(comname)
jobtitle = sheet2.cell_value( 1 , 2)
print(jobtitle)
mobno = sheet2.cell_value( 1 , 3)
print(mobno)
#print(rowcount2)
#print(colcount2)
#print(name1)"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path= "C:\\BIkash Practice\\Python\\Python38-32\\chromedriver.exe")
driver.get("https://www.orangehrm.com/")

#a= ActionChains(driver)
#m = driver.find_element_by_class_name("link")
#a.move_to_element(m).perform()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.orangehrm.com/contact-sales/")
"""driver.minimize_window()
driver.implicitly_wait(3)
#driver.maximize_window()
driver.find_element_by_id("Form_submitForm_FullName").send_keys(name1)
driver.implicitly_wait(3)
driver.find_element_by_id("Form_submitForm_CompanyName").send_keys("freelancer")
driver.implicitly_wait(3)
driver.find_element_by_id("Form_submitForm_JobTitle").send_keys("QA")
driver.implicitly_wait(3)
e = Select(driver.find_element_by_id("Form_submitForm_NoOfEmployees"))
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