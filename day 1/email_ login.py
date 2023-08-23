import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv = Service("C:\Drivers\chromedriver_win32(1)\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S185183464%3A1690561790175871&hl=en-GB&ifkv=AeDOFXgyZ6L5A5A_z-hgVFQvOPJN1eRXD_j6uIfP4znpF4Dsi-eiCViBBtCsy2QnzTOroH6BjdiE&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("elagalajanardhan@gmail.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button").click()
driver.find_element(By.NAME,"Passwd").send_keys("Jana@5268")
time.sleep(8)
driver.close()