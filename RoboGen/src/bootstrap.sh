#!/bin/sh
export FLASK_APP=controller.py
. $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 -p 3000
