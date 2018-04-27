#!/usr/bin/env python
"""
This script demostrates lifecycle of VM
* list existing VMs
* create VM
* wait until VM is running
* delete VM
"""
from pprint import pprint

from kubernetes import watch
from kubevirt import V1DeleteOptions

from examplelib import get_client, read_yaml_file


NAMESPACE = "default"


def main():
    api = get_client()

    # List existing VMs
    pprint(api.list_namespaced_virtual_machine_0(NAMESPACE))

    # Create new one
    vm_body = read_yaml_file("vm-ephemeral.yaml")
    pprint(api.create_namespaced_virtual_machine_0(vm_body, NAMESPACE))

    # Wait until VM is running
    def event_source(**kw):
        if '_request_timeout' not in kw:
            kw['_request_timeout'] = 60
        return api.list_namespaced_virtual_machine_0(NAMESPACE, **kw)

    w = watch.Watch()
    for event in w.stream(event_source):
        pprint(event)
        if event['object']['metadata']['name'] != vm_body['metadata']['name']:
            # This is not our VM
            continue
        if event['type'] == 'MODIFIED':
            if event['object']['status'].get('phase', "") == "Running":
                break  # VM is running
    w.stop()

    # Delete VM
    pprint(
        api.delete_namespaced_virtual_machine_0(
            V1DeleteOptions(), NAMESPACE, vm_body['metadata']['name']
        )
    )


if __name__ == "__main__":
    main()
