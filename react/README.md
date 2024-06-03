## 签名证书

```shell
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt -config openssl.cnf
```

### openssl.cnf

```text
[ req ]
default_bits       = 2048
distinguished_name = req_distinguished_name
req_extensions     = req_ext
x509_extensions    = v3_ca
prompt = no

[ req_distinguished_name ]
countryName                = US
stateOrProvinceName        = California
localityName               = San Francisco
organizationName           = My Company
organizationalUnitName     = IT
commonName                 = 127.0.0.1

[ req_ext ]
subjectAltName = @alt_names

[ v3_ca ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1   = 127.0.0.1
```
