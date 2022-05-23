from selenium import webdriver
import chromedriver_autoinstaller
import msvcrt as m

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib
#import urllib2

import csv
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get("https://ancientbeast.com/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "game")))

iframe = driver.find_element(by=By.NAME,value='game')

driver.switch_to.frame(iframe)

f = open("ResultadosStartUp.txt", "w")

delay=2
#aqui comienzan las iteraciones

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 1
    for row in csv_reader:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[1]/div[1]/div/label[2]")))
        num1 = driver.find_element(by=By.XPATH, value=row[0])
        num2 = driver.find_element(by=By.XPATH, value=row[1])
        num3 = driver.find_element(by=By.XPATH, value=row[2])
        num4 = driver.find_element(by=By.XPATH, value=row[3])
        num5 = driver.find_element(by=By.XPATH, value=row[4])
        num6 = driver.find_element(by=By.XPATH, value=row[5])
        num7 = driver.find_element(by=By.XPATH, value=row[6])
        num8 = driver.find_element(by=By.XPATH, value=row[7])
        start = driver.find_element(by=By.XPATH,value= "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[3]/button")#numero unidades activas

        num1.click()
        num2.click()
        num3.click()
        num4.click()
        num5.click()
        num6.click()
        num7.click()
        num8.click()
        start.click()

        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[1]/form/div[1]/div[1]/div/label[2]")))
            print("Caso de Prueba N°"+str(line)+" status: Exitoso")
            f.write("Caso de Prueba N°"+str(line)+" status: Exitoso\n")
        except TimeoutException:
            print("Caso de Prueba N°"+str(line)+" status: Fallido")
            f.write("Caso de Prueba N°"+str(line)+" status: Fallido\n")
        line+=1
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "game")))
        iframe = driver.find_element(by=By.NAME,value='game')
        driver.switch_to.frame(iframe)
f.close()
driver.quit()
















        

