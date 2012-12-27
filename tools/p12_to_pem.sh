#!/bin/sh

echo "$#"

if [ "$#" -eq '2' -a -f "$1" -a ! -f "$2" ] ; then
    openssl pkcs12 -clcerts -nokeys -out tmp-cert.pem -in "$1" &&
    openssl pkcs12 -nocerts -out tmp-cert-key.pem -in "$1" &&
    openssl rsa -in tmp-cert-key.pem -out tmp-cert-key-noenc.pem &&
    cat tmp-cert.pem tmp-cert-key-noenc.pem > "$2" &&
    rm -f tmp-cert*.pem
else
    echo "usage: $0 p12file pemfile\n";
fi
