#!/usr/bin/env python
"""
This script demostrates lifecycle of VM
* list existing VMs
* create VM
* wait until VM is running
* delete VM
"""
from pprint import pprint

from kubevirt import V1DeleteOptions

import examplelib as el


NAMESPACE = "default"


def main():
    api = el.get_client()

    # List existing VMs
    pprint(api.list_namespaced_virtual_machine(NAMESPACE))

    # Create new one
    vm = el.read_yaml_file("vm-ephemeral.yaml")
    pprint(api.create_namespaced_virtual_machine(vm, NAMESPACE))

    # Wait until VM is running
    try:
        w = el.Watch(api.list_namespaced_virtual_machine, NAMESPACE)
        vm = w.wait_for_item(
            el.get_name(vm), timeout=60,
            success_condition=lambda e:
                el.get_status(e['object']) == "Running"
        )
    except el.WaitForTimeout:
        vm = el.read_namespaced_virtual_machine(el.get_name(vm), NAMESPACE)
        raise Exception(
            "VM is not in expected state: %s != %s" % (
                el.get_status(vm), "Running"
            )
        )

    # Delete VM
    pprint(
        api.delete_namespaced_virtual_machine(
            V1DeleteOptions(), NAMESPACE, el.get_name(vm)
        )
    )


if __name__ == "__main__":
    main()
