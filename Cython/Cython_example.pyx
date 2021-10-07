import math as pymath
from libc.math cimport sin, cos, atan2
from cython.parallel import prange, threadid
from libc.stdio cimport printf

cpdef test_pure(x):
    for i in range(0,x):
        for a in range(-360,360):
            pymath.sin(a)
            pymath.cos(a)
            pymath.atan2(a,-a)


cpdef void test_datatypes(int x):
    cdef int i
    cdef int a 
    for i in range(0,x):
        for a in range(-360,360):
            pymath.sin(a)
            pymath.cos(a)
            pymath.atan2(a,-a)

cpdef void test_cmath(int x):
    cdef int i
    cdef int a
    for i in range(0,x):
        for a in range(-360,360):
            sin(a)
            cos(a)
            atan2(a,-a)

cpdef void test_nogil(int x) nogil:
    cdef int i
    cdef int a
    for i in range(0,x):
        for a in range(-360,360):
            sin(a)
            cos(a)
            atan2(a,-a)

cpdef void test_multicore(int x) nogil:
    cdef int i
    cdef int a
    for i in prange(x, nogil=True):
        for a in range(-360,360):
            sin(a)
            cos(a)
            atan2(a,-a)    