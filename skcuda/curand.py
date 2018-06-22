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

def curandCreateGenerator():
    """
    Create new random number generator.

    C Arguments:
        curandGenerator_t* generator
        curandRngType_t rng_type
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandCreateGeneratorHost():
    """
    Create new host CPU random number generator.

    C Arguments:
        curandGenerator_t* generator
        curandRngType_t rng_type
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandCreatePoissonDistribution():
    """
    Construct the histogram array for a Poisson distribution.

    C Arguments:
        double  lambda
        curandDiscreteDistribution_t* discrete_distribution
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandDestroyDistribution():
    """
    Destroy the histogram array for a discrete distribution (e.g. Poisson).

    C Arguments:
        curandDiscreteDistribution_t discrete_distribution
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandDestroyGenerator():
    """
    Destroy an existing generator.

    C Arguments:
        curandGenerator_t generator
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass


def curandGenerate():
    """
    Generate 32-bit pseudo or quasirandom numbers.

    C Arguments:
        curandGenerator_t generator
        unsigned int* outputPtr
        size_t num
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateLogNormal():
    """
    Generate log-normally distributed floats.

    C Arguments:
        curandGenerator_t generator
        float* outputPtr
        size_t n
        float  mean
        float  stddev
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateLogNormalDouble():
    """
    Generate log-normally distributed doubles.

    C Arguments:
        curandGenerator_t generator
        double* outputPtr
        size_t n
        double  mean
        double  stddev
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateLongLong():
    """
    Generate 64-bit quasirandom numbers.

    C Arguments:
        curandGenerator_t generator
        unsigned long long* outputPtr
        size_t num
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateNormal():
    """
    Generate normally distributed doubles.

    C Arguments:
        curandGenerator_t generator
        float* outputPtr
        size_t n
        float  mean
        float  stddev
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass


def curandGenerateNormalDouble():
    """
    Generate normally distributed doubles.

    C Arguments:
        curandGenerator_t generator
        double* outputPtr
        size_t n
        double  mean
        double  stddev
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGeneratePoisson():
    """
    Generate Poisson-distributed unsigned ints.

    C Arguments:
        curandGenerator_t generator
        unsigned int* outputPtr
        size_t n
        double  lambda
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateSeeds():
    """
    Setup starting states.

    C Arguments:
        curandGenerator_t generator
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateUniform():
    """
    Generate uniformly distributed floats.

    C Arguments:
        curandGenerator_t generator
        float* outputPtr
        size_t num
    C Returns:
        curandStatus_t CURANDAPI
    """
    pass

def curandGenerateUniformDouble():
    """
    Generate uniformly distributed doubles.

    C Arguments:
        curandGenerator_t generator
        double* outputPtr
        size_t num
    """
    pass

def curandGetDirectionVectors32():
    """
    Get direction vectors for 32-bit quasirandom number generation.

    C Arguments:
        curandDirectionVectors32_t* vectors
        curandDirectionVectorSet_t set
    """
    pass

def curandGetDirectionVectors64():
    """
    Get direction vectors for 64-bit quasirandom number generation.

    C Arguments:
        curandDirectionVectors64_t* vectors
        curandDirectionVectorSet_t set
    """
    pass

def curandGetProperty():
    """
    Return the value of the curand property.

    C Arguments:
        libraryPropertyType type
        int* value
    """
    pass

def curandGetScrambleConstants32():
    """
    Get scramble constants for 32-bit scrambled Sobol's.

    C Arguments:
        unsigned int** constants
    """
    pass

def curandGetScrambleConstants64():
    """
    Get scramble constants for 64-bit scrambled Sobol's.

    C Arguments:
        unsigned long long** constants
    """
    pass

def curandGetVersion():
    """
    Return the version number of the library.

    C Arguments:
        int* version
    """
    pass

def curandSetGeneratorOffset():
    """
    Set the absolute offset of the pseudo or quasirandom number generator.

    C Arguments:
        curandGenerator_t generator
        unsigned long long offset
    """
    pass

def curandSetGeneratorOrdering():
    """
    Set the ordering of results of the pseudo or quasirandom number generator.

    C Arguments:
        curandGenerator_t generator
        curandOrdering_t order
    """
    pass

def curandSetPseudoRandomGeneratorSeed():
    """
    Set the seed value of the pseudo-random number generator.

    C Arguments:
        curandGenerator_t generator
        unsigned long long seed
    """
    pass

def curandSetQuasiRandomGeneratorDimensions():
    """
    Set the number of dimensions.

    C Arguments:
        curandGenerator_t generator
        unsigned int  num_dimensions
    """
    pass

def curandSetStream():
    """
    Set the current stream for CURAND kernel launches.

    C Arguments:
        curandGenerator_t generator
        cudaStream_t stream
    """
    pass
