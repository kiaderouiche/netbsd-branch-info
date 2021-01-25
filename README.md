# netbsd-meta-info

Python implementation mirror of [NetBSD system-info utility][distro-info-link].

[distro-info-link]: https://github.com/kiaderouiche/netbsd-meta-info

## Installation

```bash
pip install netbsd-meta-info
```

## Usage

```bash
from nbmeta_info import NetBSDSysInfo, PkgsrcFramInfo

di = PkgsrcFramInfo()
print(di._releases)
```

## Example

current version: 2020Q3 / 27 septembre 2020
