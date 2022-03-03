# DupIO
A simple way to duplicate stdout and stderr to a file while still displaying it during the process

## Installation
`    pip install https://github.com/Noizrom/DupIO/archive/refs/tags/new1.tar.gz`

## Usage
```python
from DUPIO import DupStderr , DupStdout
DupStdout("External_file.txt" , "a+")
DupStderr("External_error_file.txt" , "a+")
```

