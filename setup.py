from setuptools import setup
from Cython.Build import cythonize

if __name__ == '__main__':
    setup(ext_modules=cythonize(["src/Python_Machine/level_save.pyx"]))