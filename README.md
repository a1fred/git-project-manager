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
Project issues
Create new `git ticket add `
Create new `git ticket close `
Create new `git ticket list `

### Wiki
Wiki pages, markdown.
Create `git wiki create`
Echo `git wiki echo`
List `git wiki list`
Open `git wiki open`


#### Under-the-hood
Data stored in `.gitproject/*` in human-readable format.
