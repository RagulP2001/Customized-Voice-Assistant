from selenium import webdriver
import time
import hashlib
from jsondecrypt import decrypt_me



def gmailLogin(username, password):
    	driver = webdriver.Chrome(executable_path="chromedriver.exe")
    	driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    
    	driver.find_element_by_name("identifier").send_keys(username)
    	#driver.find_element_by_xpath("//*[@id="'identifierNext'"]/span/span").click()
    	driver.find_element_by_id("identifierNext").click()
    
    	time.sleep(8)
    
    	driver.find_element_by_name("password").send_keys(password)
    	driver.find_element_by_id("passwordNext").click()
        
        
def campsLogin(username, password):
     try:
         driver = webdriver.Chrome(executable_path="chromedriver.exe")
         driver.get("https://www.camps.bitsathy.ac.in")
         time.sleep(9)
         driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr[6]/td/a').click()
         time.sleep(5)
         driver.find_element_by_id('identifierId').send_keys(username)
         driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
         time.sleep(5)
         # /html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button
         driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
         driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
     except Exception as e:
        print(e)
        print("Some error occurred")

def twitterLogin(username,password):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get('https://twitter.com/login')
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input').send_keys(username)
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()

def instagramLogin(username,password):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://www.instagram.com")
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()



def creden_returner(websitename):
    username, password = decrypt_me(websitename)
    return username, password


def webChecker(website):
    if(website == 'gmail'):
        username,password = creden_returner(website)
        gmailLogin(username,password)
    elif(website == 'camps'):
        username, password = creden_returner(website)
        campsLogin(username,password)
    elif(website == 'instagram'):
        username,password = creden_returner(website)
        instagramLogin(username,password)
    elif(website == 'twitter'):
        username,password = creden_returner(website)
        twitterLogin(username,password)
        #print("twitter else")
    else:
        print("We can't process this website... Check out later")