import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32(1)\chrome.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()

rd_male=driver.find_element(By.XPATH,"//*[@id='male']")
rd_femail=driver.find_element(By.XPATH,"//*[@id='female']")
print("default radio button status")
rd_male.click()
time.sleep(5)
print("After selecting male radio button")
print(rd_male.is_selected())
print(rd_femail.is_selected())
rd_femail.click()
time.sleep(5)
print("After selecting female radio button")
print(rd_femail.is_selected())
print(rd_male.is_selected())

#searchbox_element = driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
#searchbox_element.send_keys("Asus N551JK-XO076H Laptop")
#searchbox_btn = driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button")
#searchbox_btn.click()
#print("Display status:", searchbox_element.is_displayed())
#print("Enable status:", searchbox_element.is_enabled())

driver.quit()