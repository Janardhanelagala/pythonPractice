from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32(1)\chrome.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://snapdeal.com/")
driver.get("https://www.amazon.com/")
driver.back()
driver.forward()
driver.refresh()
driver.quit()