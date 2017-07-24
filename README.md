P3 Appliances
=============

A repo of tools for creating software-defined platforms for the ALaSKA P3 project.

This repo is split into two parts: 

- An Ansible Galaxy role, stackhpc.cluster-infra, which contains
  OpenStack Heat templates for creating bare metal instances configured
  for execution framework clusters.
- Ansible playbooks for integrating with OpenStack services, and creating 
  software middleware platforms on top of ALaSKA infrastructure.

Creating Infrastructure Using the Heat Templates
------------------------------------------------

The Heat templates and stackhpc.cluster-infra role are configured locally
through YAML environment files, then invoked through the
`alaska-infra.yml` playbook.

First, download and deploy the role from Ansible Galaxy:

`cd ansible ; ansible-galaxy install -r requirements.yml -p $PWD/roles`

Some example YAML template configurations are available in the `config/`
subdirectory.  To use these, some default parameters should first be
modified:

| Name | Description |
|------|-------------|
| `cluster_name` | Name of the Heat stack to be created, and also stem of the hostnames of compute and controller nodes |
| `cluster_keypair` | An existing RSA keypair that has been previously uploaded to OpenStack |
| `cluster_groups` | Definitions for the number of groups of compute nodes in the execution framework infrastructure, and how the compute nodes in each of those roles should be configured |

Infrastructure invocation then takes the form (for example): 

`ansible-playbook -e @config/openhpc.yml -i ansible/inventory ansible/cluster-infra.yml`

Once the infrastructure playbook has run to completion, an inventory
for the newly-created nodes will have been generated in the `ansible/`
subdirectory.  This inventory is suffixed with the value set in
`cluster_name`.  The cluster software can be deployed and configured
using another playbook (for example):

`ansible-playbook -e @config/openhpc.yml -i ansible/inventory_openhpc ansible/openhpc.yml`

