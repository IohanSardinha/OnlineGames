from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import shuffle

words = []
f = open("gartic.txt","r")
for word in f:
    words.append(word[0:-1])
f.close()

driver = webdriver.Opera()
driver.get('https://gartic.io/16gRTbV7')

username = driver.find_element_by_xpath('//*[@id="screens"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/label/input')
username.clear()
username.send_keys("Renata")

entendi = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/span/button')
entendi.click()

play = driver.find_element_by_xpath('//*[@id="screens"]/div/div[2]/div[2]/button/strong')
play.click()

x = input('waiting')


while True:
    try:
        shuffle(words)
        #resp = driver.find_element_by_xpath('//*[@id="chat"]/form/div/input')
        resp = driver.find_element_by_xpath('//*[@id="answer"]/form/div/input')
        for word in words:
            resp.send_keys(word)
            if(len(word) < 8):
                sleep(0.5)
            else:
                sleep(0.05*len(word))
            resp.send_keys(Keys.RETURN)
    except:
        pass

