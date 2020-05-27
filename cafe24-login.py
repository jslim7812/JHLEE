from selenium import webdriver
import time

driver = webdriver.Chrome('c:/crawling/chromedriver.exe')
driver.get('https://eclogin.cafe24.com/Shop/')

id = 'jwinnercode'
pw = '780617bsl'

time.sleep(1)
driver.execute_script("document.getElementsByName('mall_id')[0].value=\'" + id + "\'")
time.sleep(1)
driver.execute_script("document.getElementsByName('userpasswd')[0].value=\'" + pw + "\'")
time.sleep(1)
driver.find_element_by_class_name('btnSubmit').click()
