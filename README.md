[![Build Status](https://travis-ci.org/ish-xyz/vault-unsealing.svg?branch=develop)](https://travis-ci.org/ish-xyz/vault-unsealing)

# Hashicorp Vault Auto Unsealing Library

===

## Note that this library it is currently under development and some of the features described below are not working at the moment.

## Features:

The library will have a monitor function to check the status of the Vault services around the hashicorp vault cluster.

The library work with CONSUL BACKEND instance and should be run on each vault instance as a daemon.

The library will perform the auto-unsealing operation.

The library will perform the init-cluster operation.

The library will be integrated with third party software for security, notification and so on.

The first release it's written in Python 3.X.

The software will be available as Python Package.

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
  auto-unsealing: true
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

- join_timeout -> it represent the time that each "non-init" instance should wait to join an initialized cluster.
- timeout -> 
- log_file -> 


### Missing points:
**1 - SSL encryption between the application and the backend.**

**2 - SSL encryption between the application and the vault instance.**