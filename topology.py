# -*- coding: utf-8 -*-

import requests as r
import json
import os

# Ortam değişkenlerine kaydedilen credential bilgileri değişkene kaydedilir.
# Eğer bu kısımda sorun yaşarsanız saraclioglu20@itu.edu.tr adresinden benimle iletişime geçebilirsiniz.

username = os.environ.get('topology_username')
password = os.environ.get('topology_password')

# Bu kısımda daha sonra atılacak istekler için cookie oluşturulur.
login_url = "https://topology.adg.cc.itu.edu.tr:443/login"
header = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "https://topology.adg.cc.itu.edu.tr", "Content-Type": "application/x-www-form-urlencoded",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://topology.adg.cc.itu.edu.tr/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR,tr;q=0.9,de-DE;q=0.8,de;q=0.7,en-GB;q=0.6,en;q=0.5,en-US;q=0.4", "Connection": "close"}
login_data = {"username": username, "password": password, "login": "1"}
resp = r.post(login_url, headers=header, data=login_data)
session_id = resp.cookies


def checkStatus():
    global req_body, need
    # Cihazların ve Konteynerlerin Up down durumları bakılır.
    url = "https://topology.adg.cc.itu.edu.tr:443/maps/getNodeStatus"
    req_body = {"checkedNodes": {"container": [{"id": 30, "nodeId": "50884"}, {"id": 1143, "nodeId": "50888"}, {"id": 665, "nodeId": "50893"}, {"id": 86, "nodeId": "50879"}, {"id": 1018, "nodeId": "50910"}, {"id": 757, "nodeId": "50894"}, {"id": 1138, "nodeId": "50880"}, {"id": 860, "nodeId": "50895"}, {"id": 1022, "nodeId": "50905"}, {"id": 1175, "nodeId": "50920"}, {"id": 1146, "nodeId": "50928"}, {"id": 201, "nodeId": "50887"}, {"id": 1176, "nodeId": "50889"}, {"id": 1166, "nodeId": "50897"}, {"id": 1044, "nodeId": "50899"}, {"id": 1008, "nodeId": "50923"}, {"id": 752, "nodeId": "50903"}, {"id": 1010, "nodeId": "50907"}, {"id": 872, "nodeId": "50909"}, {"id": 777, "nodeId": "50882"}, {"id": 1013, "nodeId": "50924"}, {"id": 1023, "nodeId": "50881"}, {"id": 358, "nodeId": "50896"}, {"id": 1141, "nodeId": "50898"}, {"id": 1011, "nodeId": "50914"}, {"id": 100, "nodeId": "50902"}, {"id": 1017, "nodeId": "50904"}, {"id": 48, "nodeId": "50878"}, {"id": 1019, "nodeId": "50883"}, {"id": 961, "nodeId": "50885"}, {"id": 1020, "nodeId": "50908"}, {"id": 1173, "nodeId": "50919"}, {"id": 64, "nodeId": "50891"}, {"id": 195, "nodeId": "50892"}, {
        "id": 1031, "nodeId": "50912"}, {"id": 280, "nodeId": "50927"}, {"id": 632, "nodeId": "50877"}, {"id": 294, "nodeId": "50901"}, {"id": 1000, "nodeId": "50916"}, {"id": 1005, "nodeId": "50917"}, {"id": 96, "nodeId": "50921"}, {"id": 1106, "nodeId": "50886"}, {"id": 643, "nodeId": "50900"}, {"id": 1104, "nodeId": "50911"}, {"id": 1047, "nodeId": "50915"}, {"id": 902, "nodeId": "50918"}, {"id": 107, "nodeId": "50922"}, {"id": 32, "nodeId": "50925"}, {"id": 92, "nodeId": "50906"}, {"id": 400, "nodeId": "50913"}, {"id": 681, "nodeId": "50926"}], "device": [{"id": 4027, "nodeId": "50863"}, {"id": 2823, "nodeId": "50868"}, {"id": 1545, "nodeId": "50865"}, {"id": 1953, "nodeId": "50866"}, {"id": 3563, "nodeId": "50871"}, {"id": 3814, "nodeId": "50870"}, {"id": 1611, "nodeId": "50862"}, {"id": 1723, "nodeId": "50876"}, {"id": 1550, "nodeId": "50875"}, {"id": 2159, "nodeId": "50867"}, {"id": 2424, "nodeId": "50869"}, {"id": 2430, "nodeId": "50872"}, {"id": 1544, "nodeId": "50859"}, {"id": 4028, "nodeId": "50861"}, {"id": 4029, "nodeId": "50864"}, {"id": 2984, "nodeId": "50873"}, {"id": 1563, "nodeId": "50874"}]}}
    headers = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "X-Xsrf-Token": "eyJpdiI6InA1dXVcL0dkK0tRcWFUQythQzlxbWN3PT0iLCJ2YWx1ZSI6IkJJUWQwUGN6Z0twU3hBYWpibHNIXC9RS0pVR3pTK2dLNk5QdEcrSSt6V2NSak1DM2hSUnRwckhoRjI0cFQrS1pNIiwibWFjIjoiOTkzY2E1NmQ4YjY5MjFkZmI1YjBhNjM0NjVkZTUxNjJjZjdiZTU3NzRiMGIyMTFiYzBlMmVmNWIzNjdkYTI0MSJ9", "X-Csrf-Token": "kZEiUZZqU5MJNXw3pIcbfCKnd5rePgfv5qwR40Mj", "Sec-Ch-Ua-Mobile": "?0",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://topology.adg.cc.itu.edu.tr", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://topology.adg.cc.itu.edu.tr/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    node_stat = r.post(url, headers=headers, cookies=session_id, json=req_body)
    need = json.loads(node_stat.text)


def deviceMatchwithID():
    global result
    # Cihaz ID ve isimleri eşleştirilip bir dosyaya kaydedilir.
    device_id = req_body['checkedNodes']['device']
    with open("assets/devices.json", "w", encoding='UTF-8') as f:
        f.write('[')
        for device in device_id:
            member = device['id']
            url = "https://topology.adg.cc.itu.edu.tr:443/device/deviceProperties/{}".format(
                str(member))
            result = r.get(url, headers=header, cookies=session_id)
            x = result.json()[0]['hostname']['hostname']

            var1 = x.rfind(".sw.adg.cc.itu.edu.tr")
            var2 = x.rfind(".com")
            var3 = x.rfind(".itu.edu.tr")

            if var1 != -1:
                x = x[:var1]
            elif var2 != -1:
                x = x[:var2]
            else:
                if var3 != -1:
                    x = x[:var3]

            if member != 1563:  # Topolojiye yeni cihaz eklenirse bu kısım değişebilir.
                f.write(
                    '{ "Device": "' + x + '", "id": "' + str(member) + '"},\n')
            else:
                f.write('{ "Device": "' + x + '", "id": "' + str(member) + '"}')
        f.write(']')


def storeContainerData():
    # Container Id ve isimleri çekilir.

    url = "https://topology.adg.cc.itu.edu.tr:443/maps"
    headers = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "X-Xsrf-Token": "eyJpdiI6ImF4cnZ4NldsSkh4dnF3UmJZY3NRalE9PSIsInZhbHVlIjoiRzl5NUluT3FkYjBaOXN1RHkzbCtyVGliYjFrWjhWMzR5WmNsN3QrcVhQUUY3RnlicVlpRmU5eCt0RDJXam1jOCIsIm1hYyI6IjU0NzgzZWExNzgxNjE0NTIxMTc0ZWExMTQyYTk1YjAxMWEwYzA0NWU5ZDM4MjQ1MGI0ZjdkNDViMjc2NWYwNGEifQ==", "X-Csrf-Token": "mPGJND6mhORAEcdCZyuGdjY33VcWleqIiAVqr36k", "Sec-Ch-Ua-Mobile": "?0",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://topology.adg.cc.itu.edu.tr", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://topology.adg.cc.itu.edu.tr/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    jsonum = {"query": {"limit": "all", "offset": 0,
                        "order": "asc", "sort": "containerName"}}
    allData = r.post(url, cookies=session_id, headers=headers, json=jsonum)

    x = allData.text
    listio = json.loads(x)['data']
    with open("assets/database.json", "w", encoding='UTF-8') as f:
        f.write('[')
        for k in listio:
            for i in need['container'].values():
                container_we_need = int(i['id'])

    # Yer ve id bilgisi bir dosyaya kaydedilir.

                if container_we_need == int(k['id']):
                    if container_we_need != 96:  # Topolojiye yeni cihaz eklenirse bu kısım değişebilir.
                        f.write(
                            '{ "Place": "' + str(k['containerName']) + '", "id": "' + str(k['id']) + '"},\n')
                    else:
                        f.write(
                            '{ "Place": "' + str(k['containerName']) + '", "id": "' + str(k['id']) + '"}')
        f.write(']')


def DownOrUp():
    # Bu kısımda artık istekler atılıp kontroller yapılır ve rutin metni hazırlanır.
    device_and_containers = []
    with open('assets/devices.json', 'r', encoding='UTF-8') as f:
        x = json.load(f)
        listem = need['device'].values()

        for i in listem:
            if i['status'] == 0:
                for a in x:
                    if int(i['id']) == int(a['id']):
                        device_and_containers.append(a['Device'])

    with open('assets/database.json', 'r', encoding='UTF-8') as f:
        x = json.load(f)
        listem = need['container'].values()

        for i in listem:
            if i['status'] == 0:
                for a in x:
                    if int(i['id']) == int(a['id']):
                        device_and_containers.append(a['Place'])

    topology_sonuc = ""

    if len(device_and_containers) == 1:
        topology_sonuc = f'Topology\'de "{device_and_containers[0]}" düşük durumda.'

    elif len(device_and_containers) == 0:
        topology_sonuc = "Topology'de düşüklük yok."

    else:
        bos_list = []
        var1 = "Topology'de "
        var2 = " düşük durumda."

        for i in device_and_containers:

            last = int(len(device_and_containers))

            if device_and_containers.index(i) == last-2:
                var3 = '"' + device_and_containers[device_and_containers.index(
                    i)] + '" ve '
                bos_list.append(var3)

            elif device_and_containers.index(i) == last-1:
                var4 = '"' + \
                    device_and_containers[device_and_containers.index(i)] + '"'
                bos_list.append(var4)

            else:
                var5 = '"' + device_and_containers[device_and_containers.index(
                    i)] + '"' + ", "
                bos_list.append(var5)
        topology_sonuc = var1+"".join(bos_list)+var2

    return topology_sonuc


checkStatus()
deviceMatchwithID()
storeContainerData()
DownOrUp()
