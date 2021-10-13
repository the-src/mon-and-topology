from selenium import webdriver
from getpass import getpass
from time import sleep
import topology, mon

def bilgiler():
    global username, password
    username = input("Kullanıcı adınız: ")
    password = getpass("Şifre: ")

def login():
    global driver
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://mercek.itu.edu.tr")
    sleep(1)
    usernamefind = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tbUserName"]').send_keys(username)
    sleep(1)
    passwordfind = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tbPassword"]').send_keys(password)
    sleep(1)
    girisbuton = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnLogin"]').click()

def anasayfa():
    sleep(1)
    driver.find_element_by_xpath('//*[@id="tab-menu"]/div[1]/a[1]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_rptRutinIsProblemli_ctl01_lbtDetay"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lbProblemliIsEkle"]').click()
    sleep(3)
    yazi = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbRutinIs"]')
    yazi.send_keys(topology.DownOrUp() + mon.servers())

bilgiler()
login()
anasayfa()