from pwinput import pwinput as pw
import schedule
import random
from mercek import *

# Kullanıcı adı, şifre farz oldu.
username = input("Kullanıcı adınız: ")
password = pw("Şifre: ")
bilgiler(username, password)

# Asıl olayımız
def kararmercigi():
    login()
    rutinal()
    clean()
    quit()


# Schedule kütüphanesi ile zamanlama yaptık.

while 1:
    a = random.randint(a=10, b=30)
    # Belli olmayak diye de random vakitlerde attık.
    schedule.every().hour.at(f'20:{a}').do(kararmercigi)
    if schedule.run_pending() == None:
        continue
