#!/usr/bin/env python3
import os, sys
from exch_rate import exch_rate
from setuptools import setup, find_packages

s = setup(
	name='exch-rate',
	version=exch_rate.__version__,
	description='Tool to fetch exchange rates and convert foreign currencies.',
	url='https://github.com/prahladyeri/exch-rate',
	packages=find_packages(),
	entry_points = {
		"console_scripts": ["exchrate = exch_rate.exch_rate:main"],
	},
	install_requires=['requests'],
	license='MIT',
	author='Prahlad Yeri',
	author_email='prahladyeri@yahoo.com',
	)
