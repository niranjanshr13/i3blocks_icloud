#!/usr/bin/env python2
import os
from pyicloud import PyiCloudService
import time
import requests

userName = os.environ['ICLOUD_USERNAME']
passWord = os.environ['ICLOUD_PASSWORD']


def deviceCount(device):
    devices = len(dict(device))
    return devices

def findLocation(device, devices):
    for x in range(devices):
        try:
            deviceName = str(device[x]).split(':')[1].replace(' ','')
            deviceLocation = device[x].location()
            print(deviceLocation)
            deviceLatitude = deviceLocation['latitude']
            deviceLongitude = deviceLocation['longitude']
            unixTime = int(time.time())
            url = 'https://maps.googleapis.com/maps/api/js/GeocodeService.Search?5m2&1d' + str(deviceLatitude) + '&2d' + str(deviceLongitude)  + '&7sUS&9sen-US&key=AIzaSyCIDv7kXdaN-zt4bLG-h9TdWgk42HPgQ80&callback=_xdc_._rkedz2&token=86596'
            print(url)
            #url = 'https://www.findlatitudeandlongitude.com/processors/get-reverse-geocode.php?lat_in=' + str(deviceLatitude) + '&lon_in=' + str(deviceLongitude)
            #url = 'https://www.findlatitudeandlongitude.com/processors/get-reverse-geocode.php?lat_in=' + str(deviceLatitude) + '&lon_in=' + str(deviceLongitude) + '&time=' + str(unixTime)
            r = requests.get(url).text
            print(r)
            j = json.loads(r)
            d = j['results'][0]['formatted_address']
            print(d)
        except:
            pass


if __name__ == '__main__':
    L = PyiCloudService(userName,passWord)
    device = L.devices
    devices = deviceCount(device)
    findLocation(device,devices)
