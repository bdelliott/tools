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
    r = client.post("/servers", d)
    print "  %d" % r.status_code

    
def malformed_creates(client):
    malformed_create(client, None, "No body")
    malformed_create(client, [], "Empty list")
    malformed_create(client, {}, "Empty dict")

 
if __name__=='__main__':
    #client = nova_client.NovaClient("preprod")

    # create servers with malformed requests

    client = nova_client.NovaClient(host="sq", username="bde", tenant="openstack")
    malformed_creates(client)
   
