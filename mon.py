# -*- coding: utf-8 -*-

from time import sleep
import requests as r
import os
import json

username = os.environ.get('mon_username')
password = os.environ.get('mon_password')

s = r.Session()
url = "https://mon.cc.itu.edu.tr:443/NmConsole/User/LoginAjax"
head = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://mon.cc.itu.edu.tr", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://mon.cc.itu.edu.tr/NmConsole/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
datam = {"username": username, "password": password, "rememberMe": "false"}
res = s.post(url, headers=head, data=datam)
cookie = res.cookies


def groups():
    global jsonlist
    url = "https://mon.cc.itu.edu.tr:443/NmConsole/api/core/DeviceGroupManagement/0?returnHierarchy=true"
    cookies = cookie
    headers = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "Accept": "application/json", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://mon.cc.itu.edu.tr/NmConsole/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    resp = r.get(url, headers=headers, cookies=cookies)
    deviceGroups = resp.json()['DeviceGroups']
    with open('assets/groups.json','w') as f:
        jsonlist = []
        for device in deviceGroups:
            jsonlist.append(device)
        json.dump(jsonlist, f, indent=4)
def subgroups():
    url = "https://mon.cc.itu.edu.tr:443/NmConsole/api/core/DeviceAggregates"
    headers = {"Sec-Ch-Ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://mon.cc.itu.edu.tr", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://mon.cc.itu.edu.tr/NmConsole/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    
    with open('assets/groups.json', 'r') as f:
        mylist = json.load(f)
    
    with open('assets/subgroups.json', 'w') as k:
        for i in jsonlist:
            jlist = []
            body={"ParentGroupId": i['DeviceGroupId']}
            resp = r.post(url, headers=headers, cookies=cookie, json=body)
            
            for item in resp.json()['Items']:
                jlist.append(item)
            k.write(str(jlist))
groups()
subgroups()