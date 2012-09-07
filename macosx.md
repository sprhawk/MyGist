解决DNS无法解析问题
===================

> 未尝试过

/System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
搜索-launchd
下面加上一行-AlwaysAppendSearchDomains
保存后重新加载:
sudo launchctl unload /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
sudo launchctl load -F /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
