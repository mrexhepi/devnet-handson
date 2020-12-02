import requests
import json
from pprint import pprint

###### LOGIN ######

url="https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload={
  
    "aaaUser":{
        "attributes":{
            "name":"admin",
            "pwd":"ciscopsdt"
        }
    }


}

headers={
    "Content-type":"application/json"
}

response=requests.post(url,data=json.dumps(payload),headers=headers,verify=False).json()

#print(json.dumps(response,indent=2,sort_keys=True))

#parse token and sent cookies

token=response['imdata'][0]['aaaLogin']['attributes']['token']
cookie={}
cookie['APIC-cookie']=token

### GET APN ###
##### GET Application profile

url="https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

headers={
    'cache-control':'no-cache'
}

get_response=requests.get(url,headers=headers,cookies=cookie,verify=False).json()

""" koment 
with open('output.json', 'wt') as out:
    pprint(json.dumps(get_response,indent=2,sort_keys=True), stream=out)
"""
#### update description######
post_payload={
    "fvAp":{
        "attributes":{
            "descr":"",
            "dn":"uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}

post_respone=requests.post(url,headers=headers,cookies=cookie,verify=False,data=json.dumps(post_payload)).json()

get_response=requests.get(url,headers=headers,cookies=cookie,verify=False).json()

 print(json.dumps(get_response,indent=2,sort_keys=True))

