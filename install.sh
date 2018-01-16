#!/bin/bash
echo "Install Django "
version=$(python -V 2>&1 | grep -Po '(?<=Python )(.)')
if [ "$version" -lt 3 ]; then
pip install 'django>=1.11,<2.0'
else
pip install 'django>=2.0'
fi


echo "Startproject"
bin/django-admin.py startproject --template https://github.com/FeedTheWeb/django-base-template/zipball/master --extension py,md,rst config && \

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
