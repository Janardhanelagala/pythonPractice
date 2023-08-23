import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\\Drivers\\chromedriver_win32(1)\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

a = driver.find_element(By.XPATH, "//input[@id='Email']")  # finding username
a.clear()
a.send_keys("admin@yourstore.com")

b = driver.find_element(By.XPATH, "//input[@id='Password']")  # finding password
b.clear()
b.send_keys("admin")


c = driver.find_element(By.XPATH, "//button[@type='submit']")  # finding Login button
c.click()

time.sleep(5)

driver.quit()
