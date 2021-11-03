#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput --clear

celery multi restart -A config worker -B -S django -l info --autoscale=5,1 -O fair --time-limit=3600

echo "Starting app in DEBUG=$DEBUG"
gunicorn -b 0.0.0.0 -p 8000 config.wsgi:application
