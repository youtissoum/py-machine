from ast import literal_eval
from setuptools import Extension, setup
import sys

USE_CYTHON = False

from Cython.Build import cythonize

cython_name = 'Cython'
if 'Cython' in sys.modules:
    USE_CYTHON = True
print(f"INSTALLED MODULES : {sys.modules}")

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("Python_Machine.level_save", ["cython/level_save"+ext])]

if USE_CYTHON:
    print("If this causes error, try uninstall cython")
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

if __name__ == '__main__':
    setup(ext_modules=extensions)