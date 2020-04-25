import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'
i=0

data = json.loads(deviceJSON)
interface_data = data["interfaces"]["interface"]

for ipv4 in interface_data:
    try:
        gigIP = data["interfaces"]["interface"][i]["GigabitEthernet" + str(i)]['ipv4']
        for key in data["interfaces"]["interface"][i]:
            if ipaddress.ip_address(gigIP).is_private == False:
                print(key + " has an IP Address of " + str(gigIP) + " and is not a Private Address")
            else:
                print(key + " has an IP Address of " + str(gigIP) + " and is a Private Address")
            i=i+1
    except ValueError:
        break