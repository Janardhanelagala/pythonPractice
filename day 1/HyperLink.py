import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\\Drivers\\chromedriver_win32(1)\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.freejobalert.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"").click()
time.sleep(5)
driver.quit()