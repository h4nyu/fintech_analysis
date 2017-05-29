# -*- coding: utf-8 -*-
# Need virtualenv
.PHONY: all clean build database pip restore


build: 
	pip install -e .[dev]


fetch_package:	
	pip-compile requirements.in
	pip-compile dev-requirements.in

sync_package:
	pip-sync requirements.txt dev-requirements.txt

