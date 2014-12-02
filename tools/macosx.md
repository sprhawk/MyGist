解决DNS无法解析问题
===================

> 未尝试过

/System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
搜索-launchd
下面加上一行-AlwaysAppendSearchDomains
保存后重新加载:
sudo launchctl unload /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
sudo launchctl load -F /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist


MacOSX On SSD
-------------

## Trim Enabler ##
[http://www.groths.org/?page_id=322]

## Turn off local Time Machine snapshots ##
```
sudo tmutil disablelocal (sudo tmutil enablelocal)
```

## Turn off hibernation ##
```
sudo pmset -a hibernatemode 0
sudo rm /var/vm/sleepimage
```

## Set noatime flag ##
>>MacOS (like other unix-based systems) by default records last access time for every file. I.e. every time you read a file, a write is made on the filesystem to record this action. There is no point in doing it and no side effects if you disable that by mounting the root filesystem with noatime flag set. To do that create a file named for example “com.nullvision.noatime.plist” (you can pick any other name you wish) in the directory /Library/LaunchDaemons with the following content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> 
<plist version="1.0">
        <dict>
                <key>Label</key>
                <string>com.nullvision.noatime</string>
                <key>ProgramArguments</key>
                <array> 
                        <string>mount</string> 
                        <string>-vuwo</string> 
                        <string>noatime</string> 
                        <string>/</string> 
                </array> 
                <key>RunAtLoad</key> 
                <true/> 
        </dict> 
</plist> 
```
```shell
sudo chown root:wheel /Library/LaunchDaemons/com.nullvision.noatime.plist
mount | grep " / "
```
>> /dev/disk0s2 on / (hfs, local, journaled, noatime)

```bash
sudo ditto /Users /Volumes/your_hdd_name/Users
sudo mv /Users /Users.bak
sudo ln -s /Volumes/your_hdd_name/Users /Users
```

## Use RAM disk or HDD for temporary files ##


>> http://blog.alutam.com/2012/04/01/optimizing-macos-x-lion-for-ssd/


## 开启" Windows 7 USB Install disk" ##

1. 在系统信息里找到Boot ROM Version (MBP55.00AC.B03)
2. 打开Boot Camp.app/Contents/Info.plist
3. 找到<key>DARequiredROMVersions</key>, 增加一项：MBP55.00AC.B03
4. 找到<key>USBBootSupportedModels</key>， 增加一项：MBP55
5. 保存并启动BootCamp.app


Mac OSX 10.10 Yosimite
----------------------

1. 最大化: 点option键
