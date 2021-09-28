# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:42:01 2020

@author: F ANAME
"""


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


getdriver = ("https://assess.shlonline.eu/default?action=url&key=abcdd55c710236")

driver = webdriver.Chrome() 
driver.get(getdriver)

"Login"
time.sleep(2)
driver.find_element_by_xpath("//input[@name='aid']").send_keys(username)
driver.find_element_by_xpath("//input[@name='pwd']").send_keys(password)
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"returningUserLogin\"]/div/div[4]/input").click()
time.sleep(2)

"Agree with ts and cs"
driver.find_element_by_id("agreedText").click()
time.sleep(2)
driver.find_element_by_id('submitButton').click()
time.sleep(5)


"Background Information"
choices = ('/html/body/section/form/div[2]/section/div[15]/div/div[2]/select/option[4]',
           '/html/body/section/form/div[2]/section/div[17]/div/div[2]/select/option[3]',
           '/html/body/section/form/div[2]/section/div[19]/div/div[2]/select/option[4]',
           '/html/body/section/form/div[2]/section/div[21]/div/div[2]/select/option[3]',
           '/html/body/section/form/div[2]/section/div[25]/div/div[2]/select/option[3]')
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




data_ = pd.read_csv('questions_numerical.csv')
questions , answers = list(data_['0']) , list(data_['answers'])


visited = []

for i in range(18):
    # elements = driver.find_elements_by_class_name('centered')
    elements = driver.find_element(By.XPATH, '/html/body/form/section/div/div')
    
    time.sleep(2)
    # question = [e.text for e in elements]
    question = elements.text
    c = 1
    if question not in questions:
        questions.append(question)
    else:
        answer_ = questions.index(question)
        c = answers[answer_]
    print(i+1,question[:7], c)
    
    driver.find_element_by_id(f'answerTable{c}').click()
    
    driver.save_screenshot(f"screenshots/screenshot{answer_}.png")
    time.sleep(1)
    driver.find_element_by_id('continueBtn').click()
    time.sleep(1)


# stream = os.popen("python numerical_reasoning.py")




















# a =  1 #4.2 https://www.assignmentexpert.com/homework-answers/mathematics-answer-77367.pdf
# b =  3 #D   https://www.assignmentexpert.com/homework-answers/mathematics-answer-52562.pdf
# c =  3 #32770   https://www.assignmentexpert.com/homework-answers/mathematics-answer-37761.pdf
# d =  2 #43.99 https://www.assignmentexpert.com/homework-answers/mathematics-answer-45430.pdf
# e =  4 #123.5  https://www.assignmentexpert.com/homework-answers/mathematics-answer-37767.pdf
# f =  4 #7/8   https://www.assignmentexpert.com/homework-answers/mathematics-answer-67882.pdf
# g =  3 #12.5  https://www.assignmentexpert.com/homework-answers/mathematics-answer-37789.pdf
# h =  3 #264 https://www.assignmentexpert.com/homework-answers/mathematics-answer-37776.pdf
# i =  4 #2670 https://www.algebra.com/algebra/homework/Rate-of-work-word-problems/Rate-of-work-word-problems.faq.question.666040.html
# j =  3 #24 https://www.assignmentexpert.com/homework-answers/mathematics-answer-67881.pdf
# k =  1 #200 https://www.assignmentexpert.com/homework-answers/mathematics-answer-48570.pdf
# l =  1 #340 https://www.assignmentexpert.com/homework-answers/mathematics-answer-42060.pdf
# m =  2 #75 https://brainly.in/question/5822009
# n =  1 #-168 https://www.assignmentexpert.com/homework-answers/mathematics-answer-59701.pdf
# o =  2 #18 https://www.thestudentroom.co.uk/showthread.php?t=2183475
# p =  3 #September https://www.assignmentexpert.com/homework-answers/mathematics-answer-54442.pdf
# q =  3 #7 https://www.assignmentexpert.com/homework-answers/mathematics-answer-77242.pdf
# r =  3 #47 https://www.assignmentexpert.com/homework-answers/mathematics-answer-41514.pdf
# s =  3 #D https://psychometrictests.uk/shl-numerical-reasoning-test/
# t =  2 #5 https://www.jiskha.com/questions/1412067/jack-typed-80-words-per-minute-when-he-enrolled-in-a-typing-course-his-typing-speed#:~:text=His%20typing%20speed%20increased%20by,the%20course%20to%20the%20end%3F&text=84%2F80%20%3D%201.05%20or%20a%205%25%20increase%20in%20speed. 
# u =  0 #A https://www.assignmentexpert.com/homework-answers/mathematics-answer-43185.pdf



# answers = [globals()[f'{i}'] for i in list(map(chr,range(97,97+21)))]



# import pandas as pd
# df = pd.DataFrame(questions)

# df['answers'] = answers

# df.to_csv('questions.csv', index=False)
