[![Build Status](https://travis-ci.org/ish-xyz/vault-unsealing.svg?branch=develop)](https://travis-ci.org/ish-xyz/vault-unsealing)

# Hashicorp Vault Auto Unsealing Library

===

## Note that this library it is currently under development and most of the feature described below are not working at the moment.

## Features:

The library will have a monitor function to check the status of the Vault services around the hashicorp vault cluster.

The library work only with a CONSUL + VAULT configuration and should be runnned on each vault instance as a daemon.

The library will perform the auto-unsealing operation.

The library will perform the init-cluster operation.

The library will be integrated with third party software for security, notification and so on.

The first release it's written in Python 3.X.

The software will be available as Python Package.