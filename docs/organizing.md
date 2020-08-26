- `__method__` dunder method

- module (is a class) 
    - single source file
    - loaded with import
    - files
- package
    - other modules
    - other packages
    - directories

import urllib
import urllib.request
from urllib import request

- import sys.path
- sys.path.append('folder')
- import folderchild

### relative imports
- To use relative imports use from ..module
- you can only use the
- `from module import name` syntax
- relative imports can only be used to import modules within the current top-level package

- packages are modules which can contains other modules

- namespace packages are a mechanism for splitting a single python package across multiple directoris on disk
- namespace packages cannot have __init__.py

