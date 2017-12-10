Reboot a node and wait for it to return
=======================================

This role reboots a node, checks that it goes, and blocks until it
returns.  It uses availability of SSH as the measure of whether a
node has gone, and whether it has come back.

Requirements
------------

None.

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
