#!/usr/bin/env python2
import os
from geopy.geocoders import Nominatim
from pyicloud import PyiCloudService
import time
import requests

userName = os.environ['ICLOUD_USERNAME']
passWord = os.environ['ICLOUD_PASSWORD']


def deviceCount(device):
    devices = len(dict(device))
    return devices


def batteryLevel(device):
    pass



def findLocation(device, devices):
    for x in range(devices):
        try:
            deviceName = str(device[x]).split(':')[1].replace(' ','')
            deviceLocation = device[x].location()
            if deviceLocation == 'None':
                pass
            deviceLatitude = deviceLocation['latitude']
            deviceLongitude = deviceLocation['longitude']
            coordination = deviceLatitude, deviceLongitude
            location = geolocator.reverse(coordination)
            print(location)
        except:
            pass


if __name__ == '__main__':
    L = PyiCloudService(userName,passWord)
    geolocator = Nominatim()
    device = L.devices
    devices = deviceCount(device)
    findLocation(device,devices)
