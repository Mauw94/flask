#!/bin/sh
export FLASK_APP=./index.py
flask --app server --debug run -h 0.0.0.0