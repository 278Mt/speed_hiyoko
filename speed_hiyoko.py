from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
import random
import sys
import re

def insert_text(string, p=0.95):
    res = ""
    for s in string:
        err = ""
        rand = random.random()
        if rand > p:
            err = "z"

        res += s + err

    return res

esc_p = ''
esc_s = ''

try:
    num = sys.argv[1]
    try:
        if sys.argv[2] == 'p':
            esc_p = 'p'
        else:
            esc_p = ''
        try:
            if sys.argv[3] == 's':
                esc_s = 's'
            else:
                esc_s = ''
        except:
            esc_s = ''
    except:
        esc_p = ''

except:
    num = '51322'

driver_path = './chromedriver'
targer_url = 'https://typing.twi1.me/game/' + num

driver = webdriver.Chrome(driver_path)
driver.get(targer_url)

time.sleep(2)

target_xpath = '//*[@id="body-chrome"]'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

time.sleep(2)

target_xpath = '//*[@id="body-chrome"]'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

time.sleep(2)

target_xpath = '//*[@id="body-chrome"]'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

com = time.time()

input_text = "COM"

while input_text != "":

    text_target_xpath = '//*[@id="mtjAutoArea"]/div[1]/div[6]/div[2]/div[2]/div/div[3]'
    text_element = driver.find_element_by_xpath(text_target_xpath)
    input_text = text_element.text
    print(input_text)

    if esc_p == '':
        input_text = insert_text(input_text, 0.98)

    if " " in input_text:
        input_text = re.sub(" ", " ", input_text)

    element.send_keys(input_text)

    if esc_s == '':
        time.sleep(len(input_text) / 15)


print("END")

input()

driver.close()
driver.quit()

