Xcode
=====

# GDB #
```shell
dwarfdump --lookup 0x00003a04 --arch armv6 myApp.app.dSYM
atos -arch armv7 -o 'app name.app'/'app name' 0x0003b508
```

A script for lookup address in archives:
```
find_symbole.sh UUID arch addr
```

