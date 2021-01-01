import requests
from selenium import webdriver,common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
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
    element = WebDriverWait(driver,120).until(
        EC.visibility_of_element_located((By.ID,'startStopBtn'))
    )
    element.click()
    time.sleep(20)
    element = WebDriverWait(driver,120).until(element_present((By.ID,'shareArea')))
    result['ping'] = driver.find_element_by_id('pingText').get_property('innerHTML')
    result['jitter'] = driver.find_element_by_id('jitText').get_property('innerHTML')
    result['Download_speed'] = driver.find_element_by_id('dlText').get_property('innerHTML')
    result['Upload_speed'] = driver.find_element_by_id('ulText').get_property('innerHTML')
    result['Other_info'] = driver.find_element_by_id('ip').get_property('innerHTML')
    print(result)
finally:
    driver.close()