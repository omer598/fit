import csv
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import queue

class Faculty(object):
    def __init__(self):
        self.years = []
        self.name = ''
        self.subSelection = []


#thread test-recieve driver and faculty object
def exDat(driver, f):
    element = driver.find_element_by_id("select2-R1C9-container").click()
    element = driver.find_element_by_class_name("select2-search__field")
    element.send_keys(f.name)
    element.send_keys(Keys.RETURN)
    element = driver.find_element_by_name("B14").click()


def selectionToList(driver, str1):
    tmp = []
    tmp2 = []
    options = []
    addr = driver.page_source
    soup = BeautifulSoup(addr, "html5lib")

    if driver.find_elements(By.ID, str1).__len__() > 0:
        sel = soup.find('select', attrs={'name': str1})
        cNames = sel.find_all('option')
        for name in cNames:
            tmp.append(str(name))
        for t in tmp:
            e = t.find("\">")
            tmp2.append(t[e+2:])

        for t in tmp2:
            e = t.find("<")
            options.append(t[:e])
    return options


driver = webdriver.Chrome(r'C:\Users\Omri\Desktop\chromedriver.exe')
#driver = webdriver.PhantomJS(r'C:\Users\Omri\PycharmProjects\test\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("https://priel.biu.ac.il/yedion/fireflyweb.aspx?prgname=Enter_Search")
addr = driver.page_source
soup = BeautifulSoup(addr, "html5lib")
strTemp = []
faculties = []
strTemp = selectionToList(driver, "R1C9")
for c in strTemp:
    f = Faculty()
    f.name = c
    faculties.append(f)
#element = driver.find_element_by_id("select2-R1C9-container").click()
#element = driver.find_element_by_class_name("select2-search__field")
#element.send_keys(faculties[0].name)
#element.send_keys(Keys.RETURN)
#element = driver.find_element_by_name("B14").click()
#faculties[0].years = selectionToList(driver, "R1C1")
#faculties[0].subSelection = selectionToList(driver, "R1C2")
#time.sleep(3) #TODO: fix this shit
#driver.back()
for f in faculties:
    element = driver.find_element_by_id("select2-R1C9-container").click()
    element = driver.find_element_by_class_name("select2-search__field")
    element.send_keys(f.name)
    element.send_keys(Keys.RETURN)
    element = driver.find_element_by_name("B14").click()
    f.years = selectionToList(driver, "R1C1")
    f.subSelection = selectionToList(driver, "R1C2")
    time.sleep(3) #TODO: fix this shit
    driver.back()
#try - opt
for f in faculties:
    print(f.name)
    print(f.years)
    print(f.subSelection)

#tmp = []
#with open("out.csv", "w") as k:
#    writer = csv.writer(k, dialect='excel')
#    for f in faculties:
#        nameTemp = f.name
#        writer.writerow([nameTemp])
#        tmp = f.years
#        writer.writerow(tmp)
#        tmp = f.subSelection
#        writer.writerow(tmp)
#k.close()
driver.close()


