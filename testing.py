import time
import example
import Cython_example

x = 1_000

start = time.perf_counter()
example.test(x)
py = time.perf_counter() - start

start = time.perf_counter()
Cython_example.test_pure(x)
cy_pure = time.perf_counter() - start

start = time.perf_counter()
Cython_example.test_datatypes(x)
cy_datatypes = time.perf_counter() - start

start = time.perf_counter()
Cython_example.test_cmath(x)
cy_cmath = time.perf_counter() - start

start = time.perf_counter()
Cython_example.test_nogil(x)
cy_nogil = time.perf_counter() - start

start = time.perf_counter()
Cython_example.test_multicore(x)
cy_multicore = time.perf_counter() - start

print(py)
print(f"cy je {(py/cy_pure)} rychlejší než py")
print(f"cy_datatypes je {(py/cy_datatypes)} rychlejší než py")
print(f"cy_cmath je {(py/cy_cmath)} rychlejší než py")
print(f"cy_nogil je {(py/cy_nogil)} rychlejší než py")
print(f"cy_multicore je {(py/cy_multicore)} rychlejší než py")