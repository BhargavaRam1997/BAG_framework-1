# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='bag',
    version='2.0',
    description='Berkeley Analog Generator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
    ],
    author='Eric Chang',
    author_email='pkerichang@berkeley.edu',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'setuptools>=18.5',
        'PyYAML>=3.11',
        'Jinja2>=2.9',
        'numpy>=1.10',
        'networkx>=1.11',
        'pexpect>=4.0',
        'pyzmq>=15.2.0',
        'scipy>=0.17',
        'matplotlib>=1.5',
        'h5py',
    ],
    extras_require={
        'mdao': ['openmdao']
    },
    tests_require=[
        'openmdao',
        'pytest',
    ],
    package_data={
        'bag.interface': ['templates/*'],
        'bag.verification': ['templates/*'],
    },
)
