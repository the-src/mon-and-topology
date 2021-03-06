from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from shutil import rmtree
from pwinput import pwinput as pw
from time import sleep
import chromedriver_autoinstaller
import mon, topology, os

# Selenium kütüphanesinin çalışması için gerekli olan driver indirilir.
chromedriver_autoinstaller.install('.')


def bilgiler(known_username = None, known_pw = None):
    # Merceğe girmek için gerekli bilgiler bu kısımda kullanıcıdan alınır.
    global username, password
    if known_username == None and known_pw == None:
        username = input("Kullanıcı adınız: ")
        password = pw("Şifre: ")
    else:
        username = known_username
        password = known_pw
        
def clean():
    rmtree('__pycache__/')


def login():
    # Bu kısımda merceğe giriş yapılır.
    global driver
    chrome_opt = ChromeOptions()
    chrome_opt.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_opt)
    driver.get("https://mercek.itu.edu.tr")
    sleep(1)
    # Hacker görüntüsü verecek şekilde cool bir kısım :)
    for u in username:
        driver.find_element(By.XPATH,
            '//*[@id="ContentPlaceHolder1_tbUserName"]').send_keys(u)
        sleep(0.05)
    for p in password:
        driver.find_element(By.XPATH,
            '//*[@id="ContentPlaceHolder1_tbPassword"]').send_keys(p)
        sleep(0.05)
    driver.find_element(By.XPATH,
        '//*[@id="ContentPlaceHolder1_btnLogin"]').click()


def rutinal():
    # Mercek ana sayfasında rutin ekleme kısmındaki işlemler yapılır.
    global action
    action = ActionChains(driver)
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="tab-menu"]/div[1]/a[1]').click()
    sleep(1)
    driver.find_element(By.XPATH,
        '//*[@id="ctl00_ContentPlaceHolder1_rptRutinIsProblemli_ctl01_lbtDetay"]').click()
    sleep(1)
    driver.find_element(By.XPATH,
        '//*[@id="ctl00_ContentPlaceHolder1_lbProblemliIsEkle"]').click()
    sleep(3)
    yazi = driver.find_element(By.XPATH,
        '//*[@id="ctl00_ContentPlaceHolder1_tbRutinIs"]')
    # Bu kısımda mon.py ve topology.py dosyalarından gelen işlenmiş veri ekrana yazdırılır.
    rutin_mesaj = topology.DownOrUp() + ' ' + mon.servers()
    for r in rutin_mesaj:
        yazi.send_keys(r)
        sleep(0.01)
    driver.find_element(By.XPATH,
        '//*[@id="ctl00_ContentPlaceHolder1_btRutinIsEkle"]').click()
    action.key_down(Keys.END).perform()
    sleep(5)
    driver.close()


if __name__ == '__main__':
    bilgiler()
    login()
    rutinal()
    clean()
    quit()
