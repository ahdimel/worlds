#!/bin/sh
#run this file to setup virtual environment and
#install all needed python packages from requirements file
#needs to be done infrequently, such as when first cloning the local repo
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt