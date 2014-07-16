iptables
========

usage
-----

##1. trace
iptables -t raw -A PREROUTING -p udp -j TRACE

```
/etc/rsyslog.conf

kern.debug      /var/log/kern.debug
```

```shell
tail -n 20 -f /var/log/kern.debug
```

