![build](https://github.com/shubhamraj2202/webloader/actions/workflows/github-actions.yml/badge.svg?event=push)
[![codecov](https://codecov.io/gh/shubhamraj2202/webloader/branch/main/graph/badge.svg?token=X9KIXXBOAV)](https://codecov.io/gh/shubhamraj2202/webloader)
# webloader

Python utility to fetch a webpage and save it to disk
# Project Setup for Development
- `source setup.sh`

# Command to execute
`python3 fetch.py <url 1> <url 2> <url N> --metadata --archive_assets`
## sample
`python3 fetch.py --metadata --archive_assets https://www.google.com/`

Note:  
--metadata       : To print metadata of webpage  
--archive_assets : To save assets to a directory named after url  

# Trigger tests:
`python3 -m pytest`

# Uploaded On:
https://pypi.org/project/webloader/

# To use this as a python library
Run command:    `pip intall webloader`  
Run command:    `fetch <url 1> <url 2> <url N> --metadata --archive_assets`  
Sample command: `fetch --metadata --archive_assets https://www.google.com/`  
