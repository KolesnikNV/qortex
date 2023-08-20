#!/bin/bash
set -x
python manage.py makemigrations
python manage.py migrate

