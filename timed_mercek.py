from subprocess import Popen
from pwinput import pwinput as pw
import schedule
import random
from mercek import *

username = input("Kullanıcı adınız: ")
password = pw("Şifre: ")
bilgiler(username, password)

a = random.randint(a=10, b=30)


def kararmercigi():
    login()
    rutinal()
    clean()
    quit()


schedule.every().hour.at(f'20:{a}').do(kararmercigi)

while 1:
    schedule.run_pending()
