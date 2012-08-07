#!/usr/bin/env python

import eventlet
eventlet.monkey_patch()

import sys
sys.path.append(".")

import gettext
gettext.install(None)

from nova import context
from nova import db
from nova import flags
from nova.virt.xenapi import driver as xapi_driver
from nova.virt.xenapi import vm_utils

# hack a config file arg onto argv
sys.argv.insert(1, "--config-file=/etc/nova/nova.conf")
flags.parse_args(sys.argv)

instance_uuid = "2a4489d0-bce5-444f-a584-10b95c62a193"

# get full instance record:
ctx = context.get_admin_context()
instance = db.instance_get_by_uuid(ctx, instance_uuid)

# construct a xenapi driver:
driver = xapi_driver.XenAPIDriver()

# get xen opaque ref to vm:
vm_ref = driver._vmops._get_vm_opaque_ref(instance)

# get the root VDI for the instance:
session = driver._vmops._session
vdi_ref, vm_vdi_rec = vm_utils.get_vdi_for_vm_safely(session, vm_ref)

print vdi_ref

print "-"*80

print vm_vdi_rec

sz_bytes = int(vm_vdi_rec["physical_utilisation"])
print "vdi size (GB): %0.2f" % (sz_bytes/1024.0/1024.0/1024.0)

# test again with the chain concept:
sz_bytes = vm_utils._get_vdi_chain_size(session, vm_vdi_rec['uuid'])

print "chain vdi size (GB): %0.2f" % (sz_bytes/1024.0/1024.0/1024.0)

