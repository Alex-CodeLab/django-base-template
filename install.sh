#!/bin/bash
echo "Install Django "
pip install Django

echo "Startproject"
bin/django-admin.py startproject --template https://github.com/allox/django-base-template-1.8/zipball/master --extension py,md,rst config && \

mv config/ src && \

echo "Install requirements" && \
cd src && \
pip install -r requirements/local.txt && \
cp config/settings/local-dist.py config/settings/local.py && \

echo "Install completed. Create Database" && \
chmod +x manage.py  && \
./manage.py makemigrations && \
./manage.py migrate && \
./manage.py createsuperuser && \
./manage.py collectstatic && \
./manage.py runserver
