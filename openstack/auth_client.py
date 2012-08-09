import json
from optparse import OptionParser

import requests
from supernova import supernova

def _get_nova_config(nova_env):
    snova = supernova.SuperNova()
    snova.nova_env = nova_env

    # grab all the options for that environment:
    env = {}
    for k, v in snova.prep_nova_creds():
        env[k] = v

    return env


def authenticate(nova_env):
    """Authenticate with supernova-defined environment"""

    env = _get_nova_config(nova_env)

    credentials = {"username": env["NOVA_USERNAME"], "apiKey": env["NOVA_API_KEY"]}
    auth = {"RAX-KSKEY:apiKeyCredentials": credentials}
    d = {"auth": auth}
    body = json.dumps(d, indent=0)

    url = "%s/tokens" % env["NOVA_URL"]
    headers = {"Content-type": "application/json"}
    r = requests.post(url, data=body, headers=headers)
    if r.status_code != 200:
        raise Exception("auth fail: %s" % str(r))

    resp = json.loads(r.text)
    # return env info & entire response including auth token and service catalog:
    return env, resp


if __name__=='__main__':
    parser = OptionParser(usage="%prog <supernova_env")
    (opts, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("You must supply a supernova environment name.")

    env = args[0]
    print authenticate(env)
