/etc/ip-up.local

    route add 192.168.0.0/16 gw 10.0.0.1
    route add 10.0.0.0/16 gw 10.0.0.1
    route add jp2.vpnbcc.com gw 10.0.0.1
    route del -net 0.0.0.0 gw 10.0.0.1
    route add -net 0.0.0.0 gw $4


/etc/ppp/options.xl2tpd.client

    ipcp-accept-local
    ipcp-accept-remote
    refuse-eap
    require-mschap-v2
    noccp
    noauth
    idle 1800 
    mtu 1410
    mru 1410
    defaultroute
    # replacedefaultroute
    usepeerdns
    debug
    lock

    # plugin pppol2tp.ko
    # logfile /var/log/ppp-xl2tpd.log

    connect-delay 5000
    name ***
    password ***

/etc/ipsec.d/vpn.conf

    conn L2TP-PSK-CLIENT
            authby=secret
            pfs=no
            rekey=yes
            keyingtries=3
            type=transport
   
            left=%defaultroute
            leftprotoport=17/1701

            right=yourvpnserver
            rightprotoport=17/1701
            auto=add

/etc/ipsec.d/vpn.secrets

    %any yourvpnserver: PSK "shared secrets"