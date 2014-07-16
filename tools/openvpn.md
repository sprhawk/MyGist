OpenVPN
=======

Installation(on CentOS)
------------

```shell
wget http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
rpm -Uvh epel-release-6-8.noarch.rpm
```

```shell
cp /usr/share/doc/openvpn-*/sample-config-files/server.conf /etc/openvpn
```

/etc/openvpn/server.conf:

```
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"
```

```shell
mkdir -p /etc/openvpn/easy-rsa/keys
cp -rf /usr/share/openvpn/easy-rsa/2.0/* /etc/openvpn/easy-rsa
```

/etc/openvpn/easy-rsa/vars:
```
export KEY_COUNTRY="US"
export KEY_PROVINCE="NY"
export KEY_CITY="New York"
export KEY_ORG="Organization Name"
export KEY_EMAIL="administrator@example.com"
export KEY_CN=droplet.example.com
export KEY_NAME=server
export KEY_OU=server
```

```shell
cp /etc/openvpn/easy-rsa/openssl-1.0.0.cnf /etc/openvpn/easy-rsa/openssl.cnf
```

```shell
cd /etc/openvpn/easy-rsa
source ./vars
./clean-all
./build-ca
```

```shell
./build-key-server server
```

```shell
./build-dh
cd /etc/openvpn/easy-rsa/keys
cp dh1024.pem ca.crt server.crt server.key /etc/openvpn
```

```shell
cd /etc/openvpn/easy-rsa
./build-key client
```

```shell
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
service iptables save
```

/etc/sysctl.conf:

```
# Controls IP packet forwarding
net.ipv4.ip_forward = 1
```

```shell
sysctl -p
service openvpn start
chkconfig openvpn on
```

