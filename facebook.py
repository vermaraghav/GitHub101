from selenium import webdriver
from time import sleep 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Opera()
driver.get('http://www.facebook.com')
emailelement = driver.find_element_by_xpath('.//*[@id="email"]')
emailelement.send_keys(#username)
passelement = driver.find_element_by_xpath('.//*[@id="pass"]')
passelement.send_keys(#password)
elem = driver.find_element_by_xpath('.//*[@id="u_0_b"]')
elem.click()

statuselemnt = driver.find_element_by_xpath('.//*[@name="xhpc_message"')
time.sleep(5)

statuselement.send_keys('Hi There!')
time.sleep(3)

buttons = driver.find_element_by_tag_name('button')
time.sleep(5)

for button in buttons:
    if button.text == 'Post':
        button.click()
