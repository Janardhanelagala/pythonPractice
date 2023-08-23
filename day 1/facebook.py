import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("7386361080")
driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("7386361080")
driver.find_element(By.NAME,"login").click()

time.sleep(10)
driver.close()