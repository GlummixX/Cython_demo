from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "Cython_example",
        ["Cython_example.pyx"],
        extra_compile_args=['/openmp'],
        extra_link_args=['/openmp'],
    )
]

setup(
    name='Cython_example',
    ext_modules=cythonize(ext_modules),
)