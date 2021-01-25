# netbsd-branch-info

Python implementation mirror of [NetBSD system-info utility][branch-info-link].

[distro-info-link]: https://github.com/kiaderouiche/netbsd-branch-info

## Installation

```bash
pip install netbsd-branch-info
```

## Usage

```bash
from nbmeta_info import NetBSDSysInfo, PkgsrcFramInfo

di = PkgsrcFramInfo()
print(di._releases)
```

## Example

current version: 2020Q3 / 27 septembre 2020
