#!/bin/sh
#run this file to generate a list of
#all package requirements from the current environment
#needs to be done infrequently, and will overwrite the previous reqs file
pip freeze > requirements.txt