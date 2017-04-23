#!/bin/sh

pip install pip-tools
pip-compile requirements.in 
pip-compile dev-requirements.in 
pip-sync ./requirements.txt ./dev-requirements.txt
