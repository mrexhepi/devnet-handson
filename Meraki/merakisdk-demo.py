from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from pprint import pprint
import json
#get token from portal /Meraki
token='97a5a7ca14cd554fe471670395e1f23f9e4cbbd6'
meraki=MerakiSdkClient(token)

orgs=meraki.organizations.get_organizations()

for org in orgs:
    if org['name']=='student':
        orgId=org['id']

        
        print(orgId)
        pprint(orgs)
      
        