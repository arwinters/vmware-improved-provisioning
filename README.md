# vmware-improved-provisioning

Customize a Linux VM on the VMware vSphere virtualization platform.
Most tools for automation on the vSphere platform uses govmomi under the hood. 
Look at this site which tools make use of govmomi: https://github.com/vmware/govmomi

This project is a concept to fully automate the provisioning of Red Hat Enterprise Linux 7 and 8 
on the vSphere virtualization platform. In theory this codebase should also work for other Linux distributions.

I created this project for experimenting with an easy to use setup and basic configuration of a newly provisioned VM.

## How it works (in short)

First we convert the `metadata` and `userdata` into `gzip+base64` encoding. The encoded metadata and userdata are added with `govc` to the additional properties of the VM.
With a custom cloud-init datasource we will retrieve `metdata` and `userdata` with the `vmware-rpctool` which is available on the VM.
The decoded `metadata` and `userdata` will be applied to the guest operating system by cloud-init.

## Requirements

* govmomi
* ansible
* cloud-init
* python36 or higher

## Provisioning

### Network configuration

* Static configuration
* Dynamic configuration

### Instance

* Metadata
* Userdata
 
 
### Tests
* VMware vSphere 6.7 virtualization platform.
* Successfully deployed Red Hat Enterprise 7 and 8 VMs.


### Example

Create VM
```shell script
ansible-playbook -i inventory.ini main.yml --ask-vault-pass -e '{"vm_name": "vm01"}'
```

Create VM Template
```shell script
ansible-playbook -i inventory.ini template.yml --ask-vault-pass -e '{"vm_name": "vm01"}'
```

NForce-IT - A.R Winters
