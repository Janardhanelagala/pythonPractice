import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d = webdriver.Chrome()
d.get("https://www.calculator.net/gpa-calculator.html")
d.maximize_window()


time.sleep(5)
d.close()


