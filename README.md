P3 Appliances
=============

A repo of tools for creating software-defined platforms for the ALaSKA P3 project.

This repo is split into two parts: 

- OpenStack Heat templates for creating bare metal instances configured
  for the ALaSKA system.
- Ansible playbooks for integrating with OpenStack services, and creating 
  software middleware platforms on top of ALaSKA infrastructure.

Creating Infrastructure Using the Heat Templates
------------------------------------------------

The Heat templates can be used by themselves, but it makes more sense to use
them through the `alaska-infra.yml` playbook.

To do this, some non-default parameters should first be defined:

| Name | Description |
|------|-------------|
| `cluster_name` | Name of the Heat stack to be created, and also stem of the hostnames of compute and controller nodes |
| `cluster_nodecount` | Number of compute nodes to be created in the platfom cluster |
| `cluster_keypair` | An existing RSA keypair that has been previously uploaded to OpenStack |

These should be set in an Ansible extra variables YAML file.

Invocation then takes the form: 

`ansible-playbook -e @openhpc-stig.yml -i inventory alaska-infra.yml`

