from time import sleep
import requests
import os

username = os.environ.get('mon_username')
password = os.environ.get('mon_password')

r = requests.get(r'https://mon.cc.itu.edu.tr/NmConsole/#v=Reporting_fullpagepanel_FullPagePanel/p=%7B%22reportClass%22%3A%22Wug_report_devicemaintenancemode_DeviceMaintenanceModeReport%22%2C%22isMainView%22%3Atrue%7D')
pass
