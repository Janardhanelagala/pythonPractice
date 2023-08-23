from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\Drivers\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")
driver.maximize_window()

title = driver.title

if title == "OrangeHR":
    print("Web Page title is Verified")
else:
    print("Web Page title is not Verified")

print(driver.current_url)
driver.quit()