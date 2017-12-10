Reboot a node and wait for it to return
=======================================

This role applies a NIC firmware upgrade for Mellanox NICs.

Requirements
------------

Mellanox MFT should be installed in the software image.

Role Variables
--------------

`reboot_down_timeout`: Timeout for node shutdown.  Default is 120 seconds.

`reboot_up_timeout`: Timeout for node restart.  Default is 600 seconds.


Dependencies
------------

None.

Example Playbook
----------------


Author Information
------------------

- Stig Telfer (<stig@stackhpc.com>)
