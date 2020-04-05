import json
from selenium import webdriver
from random import randint as ri
from os import path
import unicodedata

data = {}
driver = ''

def main():
    if not path.exists('stopots.json'):
        f = open('stopots.json','w')
        f.write('{}')
        f.close()
    
    file = open("stopots.json",'r')
    global data
    data = json.loads(file.read())
    file.close()
    i = input("Abrir navegador - 0\nJogar - 1\nPovoar - 2\nVer - 3\nCopiar categoria - 4\nSair - 5\n>")
    if(i == '0'):
        browser()
    elif(i == '1'):
        play()
    elif(i == '2'):
        insert()
    elif(i == '3'):
        show()
    elif(i == '4'):
        copy()
    elif not driver == '':
        driver.quit()
        return
    else:
        return

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def save():
    file = open('stopots.json','w')
    file.write(json.dumps(data))
    file.close()

def addCategory(c):
    global data
    if not c in data.keys():
        data[c] = {}
        for i in range(ord('a'),ord('z')+1):
            data[c][chr(i)] = []

def browser(ret = main):
    global driver
    url = input('URL\n>')
    if 'https://' not in url:
        url = 'https://' + url

    driver = webdriver.Opera()
    driver.get(url)
    ret()

def play():
    if driver == '':
        browser(play)

    while True:
        l = input('Letra\n0 - sair\n1 - avaliar/estou pronto)\n>').lower()
        
        if l == '0':
            break
        if l == '1':
            btn = driver.find_element_by_xpath('//*[@id="screenGame"]/div[2]/div[2]/div/button/strong')
            btn.click()

        for i in range(1,13):
            tema = driver.find_element_by_xpath('//*[@id="screenGame"]/div[2]/div[2]/div/div[1]/label[{}]/span'.format(i)).text        
            tema = strip_accents(tema).lower()
            addCategory(tema)
            inp = driver.find_element_by_xpath('//*[@id="screenGame"]/div[2]/div[2]/div/div[1]/label[{}]/input'.format(i))
            if (tema in data.keys() and len(data[tema][l]) > 0):
                inp.send_keys(data[tema][l][ri(0,len(data[tema][l])-1)])          
    save()
    main()
    
def insert():
    global data
    while True:
        c = input("Categoria (0 sair)\n>").lower()
        if c == '0':
            break
        while True:
            if not c in data.keys():
                data[c] = {}
                for i in range(ord('a'),ord('z')+1):
                    data[c][chr(i)] = []
            l = input("\tLetra (0 sair)\n\t>").lower()
            if l == '0':
                break
            while True:
                p = input('\t\tPalavra (0 sair)\n\t\t>').lower()
                if p == '0':
                    break
                data[c][l].append(p)
    save()
    show()
    

def show():
    while True:
        print(list(data.keys()))
        c = input('Categoria (0 sair)\n>').lower()
        if c == '0':
            break
        if len(c) > 3 and c[-3:] == ' -a':
            print(data[c[0:-3]])
            continue
        while True:
            l = input('\tLetra (0 sair)\n\t>').lower()
            if l == '0':
                break
            print(data[c][l])
    main()

def copy():
    global data
    while True:
        n = input("Nova (0 sair)\n>").lower()
        if n == '0':
            break
        a = input("Antiga\n>").lower()
        data[n] = data[a]
    save()
    show()

if __name__ == '__main__':
    main()
