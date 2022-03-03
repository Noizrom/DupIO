# DupIO
A simple way to duplicate stdout and stderr to a file while still displaying it during the process

## Installation
```bash
pip install https://github.com/Noizrom/DupIO/archive/refs/tags/new1.tar.gz
```

## Usage
### Importing
```python
from DuplicateIO import DupStderr , DupStdout
```
### Initializing
```python
DupStdout("External_file.txt" , "a+")
DupStderr("External_error_file.txt" , "a+")
```

