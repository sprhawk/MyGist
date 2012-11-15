Bootloader
==========


Windows 7 & 8
-------------------
使用Windows 7安装盘引导
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd


Grub
----
* command line
    set root=(hd2,msdos5)
    linux /boot/vmlinuz root=/dev/sda5
    initrd /boot/initrd
    boot

* /etc/default/grub
    GRUB_DEFAULT=saved

    update-grub2
    grub-set-default 1/2/3
