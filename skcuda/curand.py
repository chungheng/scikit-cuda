#!/usr/bin/env python

"""
Python interface to CURAND functions.
Note: this module does not explicitly depend on PyCUDA.
"""

from __future__ import absolute_import

import re
import os
import sys
import warnings
import ctypes
import ctypes.util
import atexit
import numpy as np

from string import Template

from . import cuda
from . import utils

# Load library:
_version_list = [9.2, 9.1, 9.0, 8.0, 7.5, 7.0]
if 'linux' in sys.platform:
    _libcurand_libname_list = ['libcurand.so'] + \
                              ['libcurand.so.%s' % v for v in _version_list]
elif sys.platform == 'darwin':
    _libcurand_libname_list = ['libcurand.dylib']
elif sys.platform == 'win32':
    if sys.maxsize > 2**32:
        _libcurand_libname_list = ['curand.dll'] + \
                                  ['curand64_%s.dll' % int(10*v) for v in _version_list]
    else:
        _libcurand_libname_list = ['curand.dll'] + \
                                  ['curand32_%s.dll' % int(10*v) for v in _version_list]
else:
    raise RuntimeError('unsupported platform')

# Print understandable error message when library cannot be found:
_libcurand = None
for _libcurand_libname in _libcurand_libname_list:
    try:
        if sys.platform == 'win32':
            _libcurand = ctypes.windll.LoadLibrary(_libcurand_libname)
        else:
            _libcurand = ctypes.cdll.LoadLibrary(_libcurand_libname)
    except OSError:
        pass
    else:
        break
if _libcurand == None:
    raise OSError('curand library not found')
