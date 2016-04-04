#!/bin/bash
echo "Install Django 1.8"
pip install "Django>=1.8"

echo "Startproject"
bin/django-admin.py startproject --template https://github.com/allox/django-base-template-1.8/zipball/master --extension py,md,rst mainapp && \

mv mainapp/ src && \

echo "Install requirements" && \
cd src && \
pip install -r requirements/local.txt && \
cp mainapp/settings/local-dist.py mainapp/settings/local.py && \

echo "Install completed. Create Database" && \
chmod +x manage.py  && \
./manage.py migrate && \
./manage.py createsuperuser && \
./manage.py collectstatic && \
./manage.py runserver
