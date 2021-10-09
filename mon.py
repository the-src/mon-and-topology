from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from lxml import etree, html
import requests

username = "mon"
password = "alseup19"

r = requests.get(r'https://mon.cc.itu.edu.tr/NmConsole/#v=Reporting_fullpagepanel_FullPagePanel/p=%7B%22reportClass%22%3A%22Wug_report_devicemaintenancemode_DeviceMaintenanceModeReport%22%2C%22isMainView%22%3Atrue%7D')

def login():
    global driver
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://mon.cc.itu.edu.tr")
    sleep(1)
    usernamefind = driver.find_element_by_xpath('//*[@id="textfield-1019-inputEl"]').send_keys(username)
    sleep(1)
    passwordfind = driver.find_element_by_xpath('//*[@id="textfield-1020-inputEl"]').send_keys(password)
    sleep(1)
    girisbuton = driver.find_element_by_xpath('//*[@id="button-1022"]').click()

def bakım():
    soup = BeautifulSoup(r.content, 'html.parser')
    items = soup.find_all('table', attrs={'id':'gridview-9139-record-11618'})
    print(items)

#def allbody():
#    sleep(4)
#    content = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]')
#    i = 0
#    for table in content.find_elements_by_tag_name("table"):
#        i+=1
#        print("-"*20)
#        print(i)
#        try:
#            print(table.text)
#        except:
#            pass
#        print("-"*20)
#login()
#allbody()
bakım()