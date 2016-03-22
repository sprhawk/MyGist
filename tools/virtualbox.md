Virtualbox
==========

VBoxManage controlvm a88960c8-40e0-43ce-9ef4-139311a14770 poweroff
VBoxManage snapshot a88960c8-40e0-43ce-9ef4-139311a14770 restore test
#VBoxManage startvm a88960c8-40e0-43ce-9ef4-139311a14770 --type=headless

Compacting VirtualBox Disk Images - Windows Guests
----------------------------------------------

    1. remove unused files
    2. defragment
    3. SDelete
    4. VBoxManage modifyhd /path/to/vdi --compact
