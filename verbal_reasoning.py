# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:42:01 2020

@author: F ANAME
"""

import random
import html5lib
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import pandas as pd
import os

username = "RedThatoKK"
password = "2801239647@Tj"


getdriver = ("https://www.shl.com/shldirect/en/practice-tests/")


"Open browser"
driver = webdriver.Chrome() 
driver.get(getdriver)
time.sleep(3)

"Choose test"
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[1]/table/tbody/tr/td[2]/div[2]/div[3]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[1]/table/tbody/tr/td[2]/div[2]/div[3]/div[2]/p[2]/a').click()
time.sleep(2)

"Login"
driver.find_element_by_xpath("//input[@name='aid']").send_keys(username)
driver.find_element_by_xpath("//input[@name='pwd']").send_keys(password)
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"returningUserLogin\"]/div/div[4]/input").click()
time.sleep(2)

"Agree with ts and cs"
driver.find_element_by_id("agreedText").click()
time.sleep(2)
driver.find_element_by_id('submitButton').click()
time.sleep(2)


"Background Information"
choices = ('/html/body/section/form/div[2]/section/div[15]/div/div[2]/select/option[4]',
           '/html/body/section/form/div[2]/section/div[17]/div/div[2]/select/option[3]',
           '/html/body/section/form/div[2]/section/div[19]/div/div[2]/select/option[4]',
           '/html/body/section/form/div[2]/section/div[21]/div/div[2]/select/option[3]',
           )
for i in choices:
    driver.find_element_by_xpath(f'{i}').click()

time.sleep(2)
driver.find_element_by_id("navfinish").click()

"Take Assessment"
driver.find_element_by_xpath('/html/body/section/div/form/table/tbody/tr[1]/td[1]/div/a').click()

"Switch windows"
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)

"Start Evaluation"
driver.find_element_by_xpath('/html/body/section/div/form/div/button[2]/span').click()

time.sleep(2)


data_ = pd.read_csv('questions_verbal.csv')
questions2 , answers2 = list(data_['0']) , list(data_['answers'])


for i in range(30):
    # elements = driver.find_elements_by_class_name('centered')
    elements = driver.find_element(By.XPATH, '/html/body/form/section/div/div')
    
    time.sleep(0.2)
    # question = [e.text for e in elements]
    question = elements.text
    c = 1
    if question not in questions2:
        questions2.append(question)
    else:
        answer_ = questions2.index(question)
        c = answers2[answer_]
    print(i+1,question[:7], c)
    
    driver.find_element_by_id(f'answerTable{c}').click()
    
    driver.save_screenshot(f"screenshots/screenshot{answer_}.png")
    time.sleep(0.2)
    driver.find_element_by_id('continueBtn').click()
    time.sleep(0.2)



# stream = os.popen("python verbal_reasoning.py")
























# answers2 = [0]*9 + [1]*11 + [2]*10
# random.shuffle(answers2)




# import pandas as pd
# df2 = pd.DataFrame(questions2)

# df2['answers'] = answers2

# df2.to_csv('questions_verbal.csv', index=False)
