Shell
=====

```shell
for a in *.added; do mv $a $
{a%%.added}; done
```

防止使用未定义的变量
>> set -u
or 
>> set -o nounset

```shell
chroot=$1
...
rm -rf $chroot/usr/share/doc 
```

出错时退出shell
>> set -e
or 
>> set -o errexit

预防文件名带空格
>> if [ "$filename" = "foo" ]; 

Calculation:

```shell
    a=5
    b=`expr $a + 20`
```

Format output:

```shell
    printf "%d" 0x14000
```
