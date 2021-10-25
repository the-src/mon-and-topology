from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from shutil import rmtree
from getpass import getpass
from time import sleep
import chromedriver_autoinstaller
import topology
import mon

chromedriver_autoinstaller.install('.')

def bilgiler():
    global username, password
    username = input("Kullanıcı adınız: ")
    password = getpass("Şifre: ")


def clean():
    rmtree('__pycache__/')


def login():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://mercek.itu.edu.tr")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_tbUserName"]').send_keys(username)
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_tbPassword"]').send_keys(password)
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_btnLogin"]').click()


def anasayfa():
    global action
    action = ActionChains(driver)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="tab-menu"]/div[1]/a[1]').click()
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_rptRutinIsProblemli_ctl01_lbtDetay"]').click()
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_lbProblemliIsEkle"]').click()
    sleep(3)
    yazi = driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_tbRutinIs"]')
    yazi.send_keys(topology.DownOrUp() + ' ' + mon.servers())
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_btRutinIsEkle"]').click()
    action.key_down(Keys.END).perform()

bilgiler()
login()
anasayfa()
clean()
