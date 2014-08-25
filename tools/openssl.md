OpenSSL
======

1. sign/verify a RSA signature
--------------------------

[Link](http://www.codealias.info/technotes/openssl_rsa_sign_and_verify_howto)
####Make a Signature:
    a. Create private/public key pair:
       `openssl genrsa -out private.pem 1024`
       `openssl rsa -in private.pem -out public.pem -outform PEM -pubout`
    b. Create hash of data:
       `echo 'data to sign' > data.txt`
       `openssl dgst -sha256 < data.txt > hash`
    c. Sign the hash using the private key
       `openssl rsautl -sign -inkey private.pem -keyform PEM -in hash  > signature`
    
####Verify a Signature:
    a. Create hash of data
    b. Verify signature: (decryption)
       `openssl rsautl -verify -inkey public.pem -keyform PEM -pubin -in signature > verified`
    c. diff -s verified hash (should be same)

2. remove pkcs12 passphrase
---------------------------
openssl pkcs12 -in protected.p12 -nodes -out temp.pem
openssl pkcs12 -export -in temp.pem -out unprotected.p12

