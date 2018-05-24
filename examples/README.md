# Examples

This directory presents useful examples how to use client.

Examples expected `kubeconfig` located under `~/.kube/config` or specified
in `KUBECONFIG` environment variable.

These examples also uses some functionality from `kubernetes` modules
like a `Watch`.

So you need to make sure that you have kubernetes module installed. You can
simply install it using `requirements.txt`.

```bash
$ pip install -r requirements.txt
```

And then every example can be executed as following

```bash
$ python example_vms.py
```
