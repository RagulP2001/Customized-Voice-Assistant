from selenium import webdriver
import time
import hashlib

driver = webdriver.Chrome(executable_path="C:/Users/Dell/Desktop/chromedriver.exe")
driver.get("https://www.camps.bitsathy.ac.in")
        # //*[@id="form"]/table/tbody/tr[6]/td/a
driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr[6]/td/a').click()
time.sleep(5)
driver.find_element_by_id('identifierId').send_keys("pavithran.it18@bitsathy.ac.in")
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('MadianFool&Gen@01%$')
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()