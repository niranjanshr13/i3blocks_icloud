#!/usr/bin/env python3
from geopy.geocoders import Nominatim
from pyicloud import PyiCloudService
import os

# cred 
userName = os.environ['ICLOUD_USERNAME']
passWord = os.environ['ICLOUD_PASSWORD']

# batt isn't issue, can be done easily
def batteryLevel(device):
    pass

# count devices.
def deviceUUID(device):
    device = list(dict(device))
    return device
#    devices = len(dict(device))
#    return devices


def deviceName(device):
    try:
        deviceName = device.split(':')[1].replace(' ','')
        print(deviceName)
        deviceLocation = device[x].location()
        if deviceLocation == None:
            pass
        return deviceLocation
    except:
        pass


def findCoordination(device):
    deviceLocation = device.location()
    deviceLatitude = deviceLocation['latitude']
    deviceLongitude = deviceLocation['longitude']
    coordination = deviceLatitude, deviceLongitude
    return coordination


def findAddress(coordination):
    location = geolocator.reverse(coordination)
    #location.address
    houseNumber = location.raw['address']['house_number']
    road = location.raw['address']['road']
    neighbourhood = location.raw['address']['neighbourhood']
    postcode = location.raw['address']['postcode']
    #print(deviceName + ': ' + houseNumber + ',' + road + ',' + neighbourhood + ',' + postcode)
    #return(deviceName + ': ' + houseNumber + ',' + road + ',' + neighbourhood + ',' + postcode)
    return(houseNumber + ',' + road + ',' + neighbourhood + ',' + postcode)


if __name__ == '__main__':
    L = PyiCloudService(userName,passWord)
    device = L.devices
    devices = deviceUUID(device)
    for x in range(len(devices)):
        deviceNamex = deviceName(devices[x])
        print(deviceNamex)
        #findCoordinationx = findCoordination(devices[x])
        #findAddressx = findAddress(devices[x])
        #print(deviceNamex + ',' + findCoordinationx + ',' + findAddressx)
    #geolocator = Nominatim()
    #devices = deviceCount(device)
    #findLocation(device,devices)
    #findLocation(device,devices)
