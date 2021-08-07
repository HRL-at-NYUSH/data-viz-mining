
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urllib.request import *
from urllib import request
import os
import time
import traceback
#driver.get('http://127.0.0.1:8080/ONS_SOC_occupation_coding_tool.html');
with open('real_out.txt','r',encoding='utf-8') as f:
    a = f.readlines()
    
def processing(desired_profession):
    x = '/html/body/div[1]/div/form/div[1]/div/div[5]/div/font/span/input[1]'
    e = driver.find_element_by_xpath(x)
    e.send_keys(desired_profession)
    x2 = "/html/body/div/div/form/div[1]/div/div[5]/div/font/span/input[2]"
    e2 = driver.find_element_by_xpath(x2)
    e2.click()

def print_out(desired_profession):
    try:
        xv1 = "/html/body/div/div/form/div[1]/div/div[6]/div/font/span/span[1]"
        ev1 = driver.find_element_by_xpath(xv1)
        txv1 = ev1.text
    except:
        txv1 = ''

    try:
        xv2 = "/html/body/div/div/form/div[1]/div/div[6]/div/font/span/span[2]"
        ev2 = driver.find_element_by_xpath(xv2)
        txv2 = ev2.text
    except:
        txv2 = ''
    try:
        xv3 = "/html/body/div/div/form/div[1]/div/div[6]/div/font/span/span[3]"
        ev3 = driver.find_element_by_xpath(xv3)
        txv3 = ev3.text
    except:
        txv3 = ''
    with open('output_700.txt','a',encoding='utf-8') as f:
        f.write(desired_profession.replace('\n','')+"\t"+txv1+"\t"+txv2+"\t"+txv3+'\n')

single_times = 5
start = 700
while start<800:

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe', chrome_options=options)
    web = ['http://127.0.0.1:8080/ONS_SOC_occupation_coding_tool.html']*single_times
    for w in web:
        js = 'window.open("%s")' % w
        driver.execute_script(js)
        
    i = 1
    while i<=single_times:
        driver.switch_to.window(driver.window_handles[single_times+1-i])
        processing(a[start+i-1])
        #print_out()
        i+=1


    i = 1
    while i<=single_times:
        driver.switch_to.window(driver.window_handles[single_times+1-i])
        #processing(a[i-1])
        #print_out()
        time.sleep(4.2)
        i+=1
        
    i = 1
    while i<=single_times:
        driver.switch_to.window(driver.window_handles[single_times+1-i])
        print_out(a[start+i-1])
        #print_out()
        i+=1

    driver.quit()


    start+=single_times
    print(start)

