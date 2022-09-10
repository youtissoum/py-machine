import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    version='1.0.2',
    description="Module to run cell machine",
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.10'
    ],
    keywords='cmmm cellular automata',
    url='https://github.com/youtissoum/py-machine',
    author='youtissoum',
    author_email='youtissoum@outlook.fr',
    license='MIT',
    packages=['Python_Machine'],
    include_package_data=True
)