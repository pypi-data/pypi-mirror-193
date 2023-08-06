#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
	name='pyping3',
	version='0.0.1',
	description='A pure python ICMP ping implementation using raw sockets',
	long_description='file: README.rst',
    long_description_content_type='text/x-rst',
	license=open("LICENSE").read(),
	author="giokara",
	author_email="giokara.pyping@gmail.com",
	url='https://github.com/giokara/pyping/',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["bin/pyping"]
)
