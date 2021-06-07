#! /bin/bash
cd `dirname $0`
virtualenv venv
source venv/bin/active
pip install --no-index --find-links=./packages -r requirements.txt 