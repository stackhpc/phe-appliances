Mellanox NIC Firmware Upgrade
=============================

This role applies a NIC firmware upgrade for Mellanox NICs.

Requirements
------------

Mellanox MFT should be installed in the software image.

Role Variables
--------------

`mellanox_nic_mst`: Name of the NIC device under `/dev/mst/`. The default is
`mt4115_pciconf0`.

`mellanox_nic_fw_bin`: Path to the Mellanox firmware binary on the Ansible
control host. Required.

`mellanox_nic_fw_extra_params`: Additional arguments to provide to the
Mellanox firmware update utility, `flint`.

Dependencies
------------

None.

Example Playbook
----------------


Author Information
------------------

- Stig Telfer (<stig@stackhpc.com>)
