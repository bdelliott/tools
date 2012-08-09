import json

import requests

import auth_client

"""
Ex:

REQ: curl -i https://preprod.dfw.servers.api.rackspacecloud.com/v2/1000005/servers/detail -X GET -H "X-Auth-Project-Id: 1000005" -H "User-Agent: python-novaclient" -H "Accept: application/json" -H "X-Auth-Token: 19a3baa5-b0df-4fda-b6f4-6256a81c2de1"
"""


class NovaClient(object):

    def __init__(self, supernova_env=None, host=None, port=8774, version="1.1",
            username=None, tenant=None):
        """Given a supernova env name, authenticate and save all relevant info"""

        if supernova_env:
            self._init_via_supernova(supernova_env)

        else:
            assert host
            assert port
            assert version
            assert username
            assert tenant
           
            self.token = "%s:%s" % (username, tenant)
            self.nova_url = "http://%s:%d/v%s/%s" % (host, port, version, tenant)
            self.tenant = tenant

    def _init_via_supernova(env_name):
        env, auth = auth_client.authenticate(env_name)

        self.token = auth['access']['token']['id']

        # Get NOVA API URL:
        nova_service_name = env["NOVA_SERVICE_NAME"]
        catalog = auth['access']['serviceCatalog']

        nova_service = None
        nova_endpoint = None

        for service in catalog:
            if service['name'] == nova_service_name:
                nova_service = service
                break

        if not nova_service:
            raise Exception("No Nova service in catalog")
            
        #print nova_service

        # prune to configured region:
        region_name = env["NOVA_REGION_NAME"]
        for endpoint in nova_service['endpoints']:
            #print endpoint
            if endpoint['region'] == region_name:
                nova_endpoint = endpoint
                break

        if not nova_endpoint:
            raise Exception("Can't find correct region %s" % region_name)

        self.nova_url = nova_endpoint['publicURL']
        self.tenant = env["NOVA_PROJECT_ID"]


    def get(self, path):
        url = self.nova_url + path
        headers = self._headers()

        r = requests.get(url, headers=headers)
        assert r.status_code == 200
        d = json.loads(r.text)
        return d

    def post(self, path, d):

        url = self.nova_url + path
        print url
        body = None
        if d:
            body = json.dumps(d)

        headers = self._headers()
        r = requests.post(url, data=body, headers = headers)
        return r

    def _headers(self):
        return {
            "Content-type": "application/json",
            "Accept": "application/json",
            "X-Auth-Project-Id": self.tenant,
            "X-Auth-Token": self.token,
        }
 

if __name__=='__main__':
   client = NovaClient("preprod")
   print client.get("/servers/detail")
