from subprocess import Popen
from pwinput import pwinput as pw
import schedule
import random
from mercek import *

username = input("Kullanıcı adınız: ")
password = pw("Şifre: ")
bilgiler(username, password)


#schedule.cancel_job(job)

def kararmercigi():
    login()
    rutinal()
    clean()
    quit()

while True:
    a = random.randint(a=10, b=30)
    schedule.every().hour.at(f'20:{a}').do(kararmercigi)
    schedule.run_pending()
    continue