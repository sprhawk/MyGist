dd utility
=========

make bootable usb from iso
---------------------------

ref: https://wiki.archlinux.org/index.php/USB_flash_installation_media#In_Mac_OS_X

```
diskutil umountDisk /dev/diskXX
sudo dd if=path/to/iso of=/dev/rdiskXX bs=1m # rdisk -> raw disk, faster on macosx
diskutil eject /dev/diskXX
```

