from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://twitter.com/login')
time.sleep(6)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys('YOUR_USERNAME')
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys('YOUR_PASSWORD')
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
