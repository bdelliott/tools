import json

import nova_client


def create():

    client = nova_client.NovaClient("preprod")
    server = {
        "name": "belliott script test",
        "flavorRef": 3,
        "imageRef": "06c6a986-de1f-42e2-9670-dea1869f6525",
    }
    d = {"server": server}
    r = client.post("/servers", d)

    print d

    print "Status code: %d" % r.status_code

    d = json.loads(r.text)
    print "Response: %s" % d


create()
