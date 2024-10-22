#! /bin/bash

set -e
gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 2 manage:app