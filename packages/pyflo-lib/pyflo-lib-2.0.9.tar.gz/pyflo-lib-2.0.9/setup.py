#!/usr/bin/python3
# coding: utf-8

from setuptools import setup, find_packages


setup(name='pyflo-lib',
      version='2.0.9',
      description='Python FLO library',
      keywords='flo',
      url='https://github.com/ranchimall/pyflo',
      author='Ranchi Mall',
      author_email='ranchimallfze@gmail.com',
      license='GPL-3.0',
      packages=find_packages(),
      install_requires=['secp256k1'],
      include_package_data=True,
      package_data={
          'pyflo': ['bip39_word_list/*.txt', 'test/*.txt'],
      },
      test_suite='tests',
      zip_safe=False)
