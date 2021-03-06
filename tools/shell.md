Shell
=====

临时取消 alias

```shell
\cp ...
```

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

file name:

```shell
    basename $1
```

Substring removeal by pattern 

```shell
    ${s%*t*}
    ${s#*t*}
```

Disable alias

```shell
    \ls
```

show Git branch in prompt
```shell
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

PS1="\u:\W\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $"
```
