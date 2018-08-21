#!/usr/bin/env python
"""
This script demostrates lifecycle of VMI
* list existing VMIs and VMs
* create VMI
* wait until VMI is running
* update VMI
* delete VMI
"""
from pprint import pprint

from kubevirt import V1DeleteOptions

import examplelib as el


NAMESPACE = "default"


def main():
    api = el.get_client()

    # List existing VMs
    pprint(api.list_namespaced_virtual_machine(NAMESPACE))

    # List existing VMIs
    pprint(api.list_namespaced_virtual_machine_instance(NAMESPACE))

    # Create new one
    vmi = el.read_yaml_file("vmi-ephemeral.yaml")
    pprint(api.create_namespaced_virtual_machine_instance(vmi, NAMESPACE))

    # Wait until VM is running
    try:
        w = el.Watch(api.list_namespaced_virtual_machine_instance, NAMESPACE)
        vmi = w.wait_for_item(
            el.get_name(vmi), timeout=60,
            success_condition=lambda e:
                el.get_status(e['object']) == "Running"
        )
    except el.WaitForTimeout:
        vmi = api.read_namespaced_virtual_machine_instance(el.get_name(vmi), NAMESPACE)
        raise Exception(
            "VMI is not in expected state: %s != %s" % (
                el.get_status(vmi), "Running"
            )
        )

    # Update memory of VM
    vmi['spec']['domain']['resources']['requests']['memory'] = '512M'
    vmi = api.replace_namespaced_virtual_machine_instance(vmi, NAMESPACE, el.get_name(vmi))
    pprint(vmi)

    # Delete VM
    pprint(
        api.delete_namespaced_virtual_machine_instance(
            V1DeleteOptions(), NAMESPACE, el.get_name(vmi)
        )
    )


if __name__ == "__main__":
    main()
