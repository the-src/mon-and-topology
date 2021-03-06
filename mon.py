# -*- coding: utf-8 -*-

import requests as r
import os

# OLDU CANIM! Verileri cleartext vermicez tabiki, pathe ekleyeceksiniz, ilgili dokümanı bana ulaşırsanız atarım.
username = os.environ.get('mon_username')
password = os.environ.get('mon_password')

s = r.Session()
url = "https://mon.cc.itu.edu.tr:443/NmConsole/User/LoginAjax"
head = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://mon.cc.itu.edu.tr", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://mon.cc.itu.edu.tr/NmConsole/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
datam = {"username": username, "password": password, "rememberMe": "false"}
# Mon'a giriş yapılır.
res = s.post(url, headers=head, data=datam)
cookie = res.cookies


def servers():
    bakimlist = {}
    dusuklist = {}
    url = "https://mon.cc.itu.edu.tr:443/NmConsole/api/core/DeviceAggregates?"
    header = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://mon.cc.itu.edu.tr", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://mon.cc.itu.edu.tr/NmConsole/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    data = {"ParentGroupId": 0}
    res = r.post(url, headers=header, cookies=cookie, json=data)
    resdata = res.json()
    # ITUNET altındaki tüm cihazlar çekilir.
    for i in resdata['Items']:
        deviceId = i['DeviceId']
        deviceStatus = i['StatusState']
        deviceName = i['DisplayName']

        if deviceStatus == 3:
            continue
        # Bakımdaki veya düşük cihazların üst gruplarına bakılır.
        header = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "Accept": "application/json", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://mon.cc.itu.edu.tr/NmConsole/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
        url = "https://mon.cc.itu.edu.tr:443/NmConsole/api/core/DeviceCard?id={}&activeMonitorsCount=1".format(
            deviceId)
        resp = r.get(url, headers=header, cookies=cookie)
        json_data = resp.json()
        if deviceStatus == 2:
            try:
                bakimlist[json_data["GroupMembership"][0]["Name"]]
            except:
                bakimlist[json_data["GroupMembership"][0]["Name"]] = []
            bakimlist[json_data["GroupMembership"]
                      [0]["Name"]].append(deviceName)
        if deviceStatus == 1:
            try:
                dusuklist[json_data["GroupMembership"][0]["Name"]]
            except:
                dusuklist[json_data["GroupMembership"][0]["Name"]] = []
            dusuklist[json_data["GroupMembership"]
                      [0]["Name"]].append(deviceName)
    # Rutin mesajı formatlanır, kodun en zor kısmı burası idi benim için.
    bakim_text = 'Mon\'da '
    bakimtextler = []
    if bakimlist == {}:
        bakimtextler.append('Mon\'da sorun yok.')
    for bak in bakimlist:
        if len(bakimlist.keys()) != 1:
            if len(bakimlist[bak]) == 2:
                if bak == list(bakimlist.keys())[0]:
                    bakim_text += f'"{bak}" altında "{bakimlist[bak][0]}" ve "{bakimlist[bak][1]}", '
                elif bak == list(bakimlist.keys())[-1]:
                    bakim_text += f'"{bak}" altında "{bakimlist[bak][0]}" ve "{bakimlist[bak][1]}"'
                else:
                    bakim_text += f'"{bak}" altında "{bakimlist[bak][0]}" ve "{bakimlist[bak][1]}", '
            elif len(bakimlist[bak]) == 1:
                if bak == list(bakimlist.keys())[0]:
                    bakim_text += f'"{bak}" altında "{bakimlist[bak][0]}", '
                elif bak == list(bakimlist.keys())[-1]:
                    bakim_text += f'"{bak}" altında "{bakimlist[bak][0]}"'
                else:
                    bakim_text += f'"{bak}" altında "{bakimlist[bak][0]}", '
            else:
                if bak == list(bakimlist.keys())[-1]:
                    bakim_text += f', "{bak}" altında '
                else:
                    bakim_text += f'"{bak}" altında '
                for i in bakimlist[bak]:
                    if i == bakimlist[bak][-1]:
                        bakim_text += f've "{i}", '
                    elif i == bakimlist[bak][-2]:
                        bakim_text += f'"{i}" '
                    else:
                        bakim_text += f'"{i}", '

        elif len(bakimlist.keys()) == 1:
            bakim_text += f'"{bak}" altında '
            for b in bakimlist[bak]:
                if b == bakimlist[bak][-1]:
                    bakim_text += f'"{b}"'
                elif b == bakimlist[bak][-2]:
                    bakim_text += f'"{b}" ve '
                else:
                    bakim_text += f'"{b}", '
        if bak == list(bakimlist.keys())[-1]:
            bakim_text += " bakımda."
    bakimtextler.append(bakim_text)
    dusuk_text = ''
    dusuktextler = []
    if dusuklist == {}:
        dusuktextler.append('')
    for dus in dusuklist:
        if len(dusuklist.keys()) != 1:
            if len(dusuklist[dus]) == 2:
                if dus == list(dusuklist.keys())[0]:
                    dusuk_text += f'"{dus}" altında "{dusuklist[dus][0]}" ve "{dusuklist[dus][1]}", '
                elif dus == list(dusuklist.keys())[-1]:
                    dusuk_text += f'"{dus}" altında "{dusuklist[dus][0]}" ve "{dusuklist[dus][1]}"'
                else:
                    dusuk_text += f'"{dus}" altında "{dusuklist[dus][0]}" ve "{dusuklist[dus][1]}", '
            elif len(dusuklist[dus]) == 1:
                if dus == list(dusuklist.keys())[0]:
                    dusuk_text += f'"{dus}" altında "{dusuklist[dus][0]}", '
                elif dus == list(dusuklist.keys())[-1]:
                    dusuk_text += f'"{dus}" altında "{dusuklist[dus][0]}"'
                else:
                    dusuk_text += f'"{dus}" altında "{dusuklist[dus][0]}", '
            else:
                if dus == list(dusuklist.keys())[-1]:
                    dusuk_text += f', "{dus}" altında '
                else:
                    dusuk_text += f'"{dus}" altında '
                for i in dusuklist[dus]:
                    if i == dusuklist[dus][-1]:
                        dusuk_text += f'"{i}"'
                    elif i == dusuklist[dus][-2]:
                        dusuk_text += f'"{i}" ve '
                    else:
                        dusuk_text += f'"{i}", '

        elif len(dusuklist.keys()) == 1:
            dusuk_text += f'"{dus}" altında '
            for b in dusuklist[dus]:
                if b == dusuklist[dus][-1]:
                    dusuk_text += f'"{b}"'
                elif b == dusuklist[dus][-2]:
                    dusuk_text += f'"{b}" ve '
                else:
                    dusuk_text += f'"{b}", '
        if dus == list(dusuklist.keys())[-1]:
            dusuk_text += " düşük durumda."
    dusuktextler.append(dusuk_text)

    mon_sonuc = bakimtextler[0] + ' ' + dusuktextler[0]
    return mon_sonuc


servers()
