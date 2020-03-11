# [Discountinued as Hashicorp has integrated the auto-unsealing on the open source version]

[![Build Status](https://travis-ci.org/ish-xyz/vault-unsealing.svg?branch=develop)](https://travis-ci.org/ish-xyz/vault-unsealing)

# Hashicorp Vault Auto Unsealing Library

===

## Note that this library it is currently under development and some of the features described below are not working at the moment.

## Features:

[DONE] - The library will have a monitor function to check the status of the Vault services around the hashicorp vault cluster.

[DONE] - The library work with CONSUL BACKEND instance.

The library will be available as side-car.

The library should work with SSL and custom certificates.

The library will be available as a official python package.

[DONE] - The library will perform the auto-unsealing operation.

[DONE] - The library will perform the init-cluster operation.

The library will be integrated with third party software for security, notification and so on. * TBD *

[DONE] The first release it's written in Python 3.X.


## Installation

As long as the **Hashicorp Vault** API are reachable, you can build the container through the Dockerfile in the folder *build/* and run the auto-unsealing process as sidecar.

```
cd build/
docker build -t ishxyz-autounseal -f Dockerfile .
docker run -td --name auto-unseal ishxyz-autounseal
```

In alternative you can run the application  directly in the Hashicorp Vault instances without docker or in a remote instance calling the vault API externally.

The application **needs a consul as a backend** even if your Hashicorp Vault architecture does not require a Consul backend, the application still need it and it will try to store essential information inside the backend.
I choose consul instead of KMS or the cloud owned solution in order to have a cloud-agnostic application and don't force user to have an AWS or AZURE or GCP account.
Anyway the information in Consul are crypted and encoded with and in-transit encryption, AES.

### Env vars
To configure the app you must put some essential data inside the *config.yml* file and indicate it using the env variable called VAU_CONFIG, like that.

```
export VAU_CONFIG=/home/vault/.vau/config.yml
```

### config.yml - The config file should look like that:

```
join_timeout: 10
timeout: 10
logfile: /tmp/vault.log

vault:
  init: false
  init-payload: { "secret_shares": 5, "secret_threshold": 3 }
  path: '/v1'
  address: http://vault.io:8200

consul:
  address: http://consul.io:8500
  path: /v1/kv
  acl-token: 'very-secret-token'

secrets:
  aes: "4NHSl6fvvessx2d="
  iv: "6NgEl6fkjessx2d="

#Only needed if your cluster it has been already initialized
shamir_keys: []
root_token: ''
```

### Params:
| **NAME** | **DESCRIPTION** | **REQUIRED** | **DEFAULT** |
|---|---|---|---|
| join_timeout |it represent the time that each "non-init" instance should wait to join an initialized cluster. Represented in seconds. | true | 60 seconds |
| timeout | the timeout used to poll the API and check the VAULT status for each vault instance. Represented in seconds. | true | 10 seconds |
| log_file | Log file used to store the execution data and info. | false | none |
| vault.init | param used to determine if the Vault instance should be initialized or not | none | false |
| vault.init-payload | The payload used to initialize the cluster. see https://www.vaultproject.io/api/system/init.html | none | none |
| vault.path | The Hashicorp Vault base path used to perform the REST api calls. | true | /v1 |
| vault.address | The Hashicorp Vault instance address | true | none |
| consul.adress | The backend address, the address should be and http or https endpoint and should contain the port. | true | none |
| consul.path | Consul store prefix, normally it is "v1/". | true | v1/ |
| consul.acl-token | The token to communicate and authenticate on the Consul ACL. | true | none
| secrets.aes | A 16-bit encryption key used from the AES lib to perform the in transit encryption and decryption | true | none |
| secrets.iv | A 16-bit initialization vector  used from the AES lib to perform the in transit encryption and decryption | true | none |
| shamir_keys | ONLY if the cluster has been already initialized and they don't need to stay in the config file after the first execution | false | none | 
| root_token | ONLY if the cluster has been already initialized and it doesn't need to stay in the config file after the first execution | false | none |

### Missing points:
**1 - SSL encryption between the application and the backend.**

**2 - SSL encryption between the application and the vault instance.**
