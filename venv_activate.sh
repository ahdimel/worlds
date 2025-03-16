#!/bin/sh
#run this file to activate a virtual environment and
#install all needed python packages from requirements file
#this only works if .venv already exists in project folder.
source ./.venv/bin/activate
pip install -r requirements.txt