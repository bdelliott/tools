import json
import sys
import time

from prettytable import PrettyTable

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

    secs = end - start

    if r.status_code != 400:
        print "Bad code:  %d" % r.status_code
        print "  %0.2f" % secs

    return secs
    
def malformed_creates(client):
    malformed_create(client, None, "No body")
    malformed_create(client, [], "Empty list")
    malformed_create(client, {}, "Empty dict")

    d = {"%2e%2e%5c%2fetc%2fpasswd": []}
    malformed_create(client, d, "No server key")

    malformed_create(client, 1234, "Integer for body")
    malformed_create(client, "foobar", "String for body")


def wrong_method(client):
    # send with wrong HTTP method:
    path = "/servers?image=b142bd0c-d66d-4b6e-913b-2f7541f21eff"
    r = client.post(path, None)
    print r.status_code

    # again with a body:
    d = {"foo": "bar"}
    body = json.dumps(d)
    r = client.post(path, body)
    print r.status_code


def wrong_method_timed_newlines(client, num):
    """Time to check claim that lots of newlines somehow creates
    nonlinear API response times.
    """
    path = "/servers"

    d = {"servers": [] }
    body = json.dumps(d)
    #print body

    # shave closing '}' and insert the newlines
    body = body[:-1]
    body = body + "\n"*num
    body = body + "}"
    #print body
    start = time.time()
    r = client.post(path, d)
    end = time.time()

    secs = end - start
    return secs


if __name__=='__main__':
    #client = nova_client.NovaClient("preprod")

    # create servers with malformed requests

    client = nova_client.NovaClient(host="sq", username="bde", tenant="openstack")

    #malformed_creates(client)
    #wrong_method(client)

    #d = {"%2e%2e%5c%2fetc%2fpasswd": []}
    #malformed_create(client, d, "No server key")

    x = PrettyTable(["Num", "Secs"])        

    for num in range(0, 10000, 100):
        secs = 1000 * wrong_method_timed_newlines(client, num)
        secs = "%0.2f" % secs
        x.add_row((num, secs))    

    print x
