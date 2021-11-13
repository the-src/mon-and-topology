from datetime import datetime
import random
from mercek import *

username = input("Kullanıcı adınız: ")
password = pw("Şifre: ")
bilgiler(username, password)

def kararmercigi():
    login()
    rutinal()
    clean()
    quit()

while True:
    if datetime.now().minute == 20 and datetime.now().second == 0:
        sleep(random.randint(a=1,b=5))
        kararmercigi()
    else:
        continue
            