import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver_win32(1)\\chrome.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("student")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Password123")
driver.find_element(By.XPATH,"//button[@id='submit']").click()

time.sleep(5)
driver.close()