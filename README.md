# Git project manager
Git project manager with in-repository data storage.

## Features
* All data stored in .gitproject folder
* All data stored in human-readable format, for easy conflict resolving
* Embedded ticket system
* [TODO] Embedded WIKI
* [TODO] Cli or webui interaction

## Install
```bash
$ python3.7 setup.py install
```

## Sections
### Tickets
Create new
```bash
$ git ticket --help
```


#### Under-the-hood
Tickets stored in `.gitproject/*`.
