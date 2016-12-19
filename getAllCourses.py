from bs4 import BeautifulSoup
#import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
#from selenium.webdriver.common.keys import Keys

class Courses(object):

    def __init__(self):
        self.Cname=""
        self.Cnum=""

path = os.path.dirname(os.path.realpath("getAllCourses.py"))
phantomPath = path + "\\phantomjs.exe"
googlePath = path +"\\chromedriver.exe"
#driver = webdriver.Chrome(str(googlePath))
driver = webdriver.PhantomJS(str(phantomPath))
courses = []
tmp = []
tmp2 = []
driver.get("https://dory.os.biu.ac.il/BIH/srh.jsp")
Select(driver.find_element_by_name("degree")).select_by_value("1")
driver.find_element_by_name("search").click()
driver.find_element_by_css_selector("a[href=\"javascript:AllSearchResults()\"]").click()
addr = driver.page_source
soup = BeautifulSoup(addr, "html5lib")
table = soup.find('table', attrs={'class': 'regular_table'})
tdInTable = table.find_all("td")
for t in tdInTable:
    tmp.append(str(t))
i = 0
while i < tmp.__len__():
    tmp2.append(tmp[i])
    tmp2.append(tmp[i+1])
    i += 4
i = 0
while i < tmp2.__len__():
    e = tmp2[i].find("0\">")
    tmp2[i] = tmp2[i][e+3:]
    e = tmp2[i].find("</")
    tmp2[i] = tmp2[i][:e]
    i += 2
i = 1
while i < tmp2.__len__():
    e = tmp2[i].find("d>")
    tmp2[i] = tmp2[i][e + 2:]
    e = tmp2[i].find("</")
    tmp2[i] = tmp2[i][:e]
    i += 2
i = 0
while i < tmp2.__len__():
    c = Courses()
    c.Cname = tmp2[i+1]
    c.Cnum = tmp2[i]
    courses.append(c)
    i += 2
for c in courses:
    print(c.Cnum, c.Cname)

print(courses.__len__())

