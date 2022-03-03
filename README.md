# DupIO
A simple way to duplicate stdout and stderr to a file while still displaying it during the process

## Installation
```bash
pip install https://github.com/Noizrom/DupIO/archive/refs/tags/duplicateio-0.2.1.tar.gz
```

## Usage
### Importing
```python
from duplicateio import duplicatestdout , duplicatestderr
```
### Initializing
```python
duplicatestdout("file-to-fork-stdout.txt" , "a+")
duplicatestderr("file-to-fork-stderr.txt" , "a+")
```

