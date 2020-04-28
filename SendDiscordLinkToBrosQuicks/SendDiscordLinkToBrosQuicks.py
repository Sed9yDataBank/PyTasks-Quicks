"""
Automatically Send Discord Chat Room Link To My Friends On Facebook
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string

driver = webdriver.Firefox()
driver.get('https://discordapp.com/') #Going To Site
driver.find_element_by_css_selector('.appButton-3GZ9-9').click()


time.sleep(3) #Lets The Browser Load Just As A Precaution

discord = driver.current_url

driver.get("https://facebook.com")
time.sleep(2) #Sleeps Because Sometimes Will Not Load Fast Enough

#Login To Facebook
driver.find_element_by_id('email').send_keys('YOUR_EMAIL@gmail.com')
driver.find_element_by_id('pass').send_keys('PASSWORD')
driver.find_element_by_id('loginbutton').click()

time.sleep(3)

#This Gets The Class Name To Click On The Message Box On
#The Right Hand Side Of Facebook
driver.find_element_by_class_name("class_of_friend").click()

time.sleep(3)

#This Sends The Keys Into The Message Box Once It Has Been Created
driver.find_element_by_css_selector('css_selector_of_friend').send_keys(str(discord) , Keys.ENTER )

#Go Back To Discord
driver.get(discord)
