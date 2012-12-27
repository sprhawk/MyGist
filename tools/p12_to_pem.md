

##Convert p12 to pem format:
openssl pkcs12 -clcerts -nokeys -out apns-dev-cert.pem -in apns-dev-key.p12
openssl pkcs12 -nocerts -out apns-dev-key.pem -in apns-dev-key.p12

##Remove the password:
openssl rsa -in apns-dev-key.pem -out apns-dev-key-noenc.pem

##Combine two key and cert into one:
cat apns-dev-cert.pem apns-dev-key-noenc.pem > apns-dev.pem

