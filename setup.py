import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    version='1.0.0',
    description="Module to run cell machine",
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10.6'
    ],
    keywords='cmmm cellular automata',
    url='https://github.com/youtissoum/py-machine',
    author='youtissoum',
    license='MIT',
    packages=['Python_Machine'],
    include_package_data=True
)