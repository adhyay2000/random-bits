#!/usr/local/bin/python3.6
import requests
from selenium import webdriver,common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time,os,datetime
logging.basicConfig(filename='speedTest.log',filemode='a',format=str(datetime.datetime.now())+'%(name)s - %(levelname)s - %(message)s')
class element_present(object):
    def __init__(self,locator):
        self.locator= locator
    def __call__(self,driver):
        element = driver.find_element(*self.locator)
        if element.get_property('offsetParent') != None:
            return element
        else:
            return False

try:
    driver = webdriver.Chrome()
    driver.get('https://librespeed.org/')
    result = {}
    element = WebDriverWait(driver,60).until(
        EC.visibility_of_element_located((By.ID,'startStopBtn'))
    )
    element.click()
    element = WebDriverWait(driver,60).until(element_present((By.ID,'shareArea')))
    result['ping'] = driver.find_element_by_id('pingText').get_property('innerHTML') + 'ms'
    result['jitter'] = driver.find_element_by_id('jitText').get_property('innerHTML') + 'ms'
    result['Download_speed'] = driver.find_element_by_id('dlText').get_property('innerHTML') + 'MBps'
    result['Upload_speed'] = driver.find_element_by_id('ulText').get_property('innerHTML') + 'MBps'
    # print(result)
    os.system("notify-send 'Speed Test Results' '{}'".format(str(result)))
    driver.close()
except Exception as E:
    logging.error(E)