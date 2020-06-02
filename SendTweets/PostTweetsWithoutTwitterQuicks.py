"""
Tweet Without Twitter
"""

from selenium import webdriver
import time

username = input("Userame: ")
__username__ = f'{username}'
password = input("Password: ")
__password__ = f'{password}'
tweet = input("Tweet: ")
__tweet__ = f'{tweet}'

browser = webdriver.Firefox(r'file/to/geckodriver/if/needed/')
browser.get('https://twitter.com/login')

user = browser.find_element_by_class_name('js-username-field')
user.send_keys(__username__)
pw = browser.find_element_by_class_name('js-password-field')
pw.send_keys(__password__)
log_in = browser.find_element_by_class_name('EdgeButtom--medium')
log_in.click()
time.sleep(1)
start_tweeting = browser.find_element_by_class_name('r-e7q0ms')
start_tweeting.click()
time.sleep(1)
tweet_content = browser.find_element_by_class_name('notranslate')
tweet_content.send_keys(__tweet__)
time.sleep(1)
tweet_button = browser.find_element_by_class_name('r-1n0xq6e')
tweet_button.click()
