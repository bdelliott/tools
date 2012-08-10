import json
import sys
import time

import nova_client


def good_create(client):

    d = {
        "name": "belliott script test",
        "flavorRef": 3,
        "imageRef": "06c6a986-de1f-42e2-9670-dea1869f6525",
    }
    r = client.post("/servers", d)
    return r


def malformed_create(client, d, msg):
    print msg

    # time it:
    start = time.time()
    r = client.post("/servers", d)
    end = time.time()

    print "  %d" % r.status_code
    if r.status_code == 500:
        sys.exit(1)

    secs = end - start
    print "  %0.2f" % secs
    return secs
    
def malformed_creates(client):
    malformed_create(client, None, "No body")
    malformed_create(client, [], "Empty list")
    malformed_create(client, {}, "Empty dict")

    d = {"%2e%2e%5c%2fetc%2fpasswd": []}
    malformed_create(client, d, "No server key")


def wrong_method():
    # send with wrong HTTP method:
    path = "/servers?image=b142bd0c-d66d-4b6e-913b-2f7541f21eff"
    r = client.post(path, None)
    print r.status_code

    # again with a body:
    d = {"foo": "bar"}
    body = json.dumps(d)
    r = client.post(path, None)
    print r.status_code

 
if __name__=='__main__':
    #client = nova_client.NovaClient("preprod")

    # create servers with malformed requests

    client = nova_client.NovaClient(host="sq", username="bde", tenant="openstack")

    malformed_creates(client)
    #wrong_method()
