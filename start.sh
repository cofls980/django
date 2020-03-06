#! /bin/bash

/wait-for-it.sh db:3306 -t 10
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0:8000
