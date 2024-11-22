# Chargerwallet Firmware documentation

Welcome to the Chargerwallet Firmware repository. This repository is so called _monorepo_, it contains several different yet very related projects that together form the Chargerwallet Firmware ecosystem.

## Repository Structure

* **[`ci`](https://github.com/chargerwallet/firmware/tree/master/ci/)**: [Gitlab CI](https://gitlab.com/chargerwallet/firmware) configuration files
* **[`common/defs`](https://github.com/chargerwallet/firmware/tree/master/common/defs/)**: JSON coin definitions and support tables
* **[`common/protob`](https://github.com/chargerwallet/firmware/tree/master/common/protob/)**: Common protobuf definitions for the Chargerwallet protocol
* **[`common/tools`](https://github.com/chargerwallet/firmware/tree/master/common/tools/)**: Tools for managing coin definitions and related data
* **[`core`](https://github.com/chargerwallet/firmware/tree/master/core/)**: Chargerwallet Core, firmware implementation for Chargerwallet T
* **[`crypto`](https://github.com/chargerwallet/firmware/tree/master/crypto/)**: Stand-alone cryptography library used by both Chargerwallet Core and the Chargerwallet One firmware
* **[`docs`](https://github.com/chargerwallet/firmware/tree/master/docs/)**: Assorted documentation
* **[`python`](https://github.com/chargerwallet/firmware/tree/master/python/)**: Python client library and the `chargerwalletctl` command
* **[`storage`](https://github.com/chargerwallet/firmware/tree/master/storage/)**: NORCOW storage implementation used by both Chargerwallet Core and the Chargerwallet One firmware
* **[`tests`](https://github.com/chargerwallet/firmware/tree/master/tests/)**: Firmware unit test suite
* **[`tools`](https://github.com/chargerwallet/firmware/tree/master/tools/)**: Miscellaneous build and helper scripts
* **[`vendor`](https://github.com/chargerwallet/firmware/tree/master/vendor/)**: Submodules for external dependencies


## Contribute

- Adding a small feature or a fix
  If your change is somewhat subtle, feel free to file a PR in one of the appropriate repositories directly. See the PR requirements noted at [CONTRIBUTING.md](misc/contributing.md).
- Add new coin/token/network to the official chargerwallet firmware
  See [COINS.md](misc/COINS.md)

## Security vulnerability disclosure

- Please read [Bug Bunty Rules](https://github.com/chargerwallet/app-monorepo/blob/chargerwallet/docs/BUG_RULES.md), we have detailed the exact plan in this article.
- Please report suspected security vulnerabilities in private to dev@chargerwallet.com
- Please do NOT create publicly viewable issues for suspected security vulnerabilities.
- As an open source project, although we are not yet profitable, we try to give some rewards to white hat hackers who disclose vulnerabilities to us in a timely manner.

## Note on terminology

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).
