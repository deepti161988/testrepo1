from selenium import webdriver
from selenium.webdriver.common.by import By

import xlrd
from xlrd import sheet

workbook = xlrd.open_workbook("testsheets.xls")
sheet = workbook.sheet_by_name("S1")

Rows = sheet.nrows
Columns = sheet.ncols
print(Rows)
print(Columns)

import time
driver = webdriver.Chrome(executable_path = "C:\\BIkash Practice\\Python\\Python38-32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/")
driver.find_element (By.ID , 'myText').send_keys('pat@gmail.com')

driver.close()