#from selenium.webdriver import Chrome

from selenium import webdriver
import chromedriver_autoinstaller
import msvcrt as m

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time

def wait():
    m.getch()

#driver = Chrome()
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get("https://ancientbeast.com/")

print(driver.current_url)

delay = 2
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "game")))


#time.sleep(4)

iframe = driver.find_element(by=By.NAME,value='game')

driver.switch_to.frame(iframe)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[1]/div[1]/div/label[2]")))


search = driver.find_element(by=By.XPATH,value= "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[1]/div[1]/div/label[1]")#1vs1 o 2vs2

search2 = driver.find_element(by=By.XPATH,value= "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[1]/div[2]/div/label[4]")#numero unidades activas

search3 = driver.find_element(by=By.XPATH,value= "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[1]/div[3]/div/label[1]")#numero unidades activas

search4 = driver.find_element(by=By.XPATH,value= "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[3]/button")#numero unidades activas

search.click()
search2.click()
search3.click()
search4.click()

wait()

driver.quit()
