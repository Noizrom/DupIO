![Lines](https://img.shields.io/tokei/lines/github/Noizrom/DupIO?style=flat-square)
# DupIO
A simple way to duplicate stdout and stderr to a file while still displaying it during the process

## Installation
```bash
pip install https://github.com/Noizrom/DupIO/archive/refs/tags/duplicate_io-v0.3.0.tar.gz
```

## Usage
### Importing
```python
from duplicate_io import Forkstdout , Forkstderr
```
### Initializing
```python
Forkstdout("file-to-fork-stdout.txt" , "a+")
Forkstderr("file-to-fork-stderr.txt" , "a+")
```

