
# from urllib import request
import requests
import Meraki_info
import json

base_url = Meraki_info.base_url
api_key = Meraki_info.api_key

def Get_Organization():
    url_org = f"{base_url}/organizations"
    

    header = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : api_key
    }

    response = requests.get(url=url_org, headers=header)

    data = response.json()
    print (json.dumps(data, indent=4))

def Get_org_inventory_device():
    #  /organizations/{organizationId}/inventory/devices
    Org_id = "463308"

    url = f"{base_url}/organizations/{Org_id}/inventory/devices"

    header = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : api_key
    }

    response = requests.get(url=url, headers=header)
    data = response.json()
    print (json.dumps(data, indent=4))

def Get_device_null():
    Org_id = "463308"

    url = f"{base_url}/organizations/{Org_id}/inventory/devices"
    header = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : api_key
    }
    response = requests.get(url=url, headers=header)
    data = response.json()

    num = len (data)
    print (num)
    data_device_null =[]

    for i in range(num):
        Network_ID = data[i]["networkId"]
        print (Network_ID)
        if Network_ID == None:
            data_device_null.append(data[i])
        print (data_device_null)

        






if __name__ == '__main__':
    Get_Organization()
    Get_org_inventory_device()
    Get_device_null()
