
# Django 1.8 Project Template - Bootstrap3, Allauth#

## About ##

This 'best practice' template is based off of the work of Mozilla Playdoh, 
Two Scoops of Django and [django-base-template](https://github.com/xenith/django-base-template). 
It aims to be simple, yet complete.

This version of the project template includes new options for Django 1.8

## Installation ##


- Make sure you have libffi installed 
   - $ sudo apt-get install libffi-dev
- (python3) Make sure you have libevent-dev, python3-dev  installed 
   - $ sudo apt-get install libevent-dev python3-dev
- Create your working environment and virtualenv:
   - $ virtualenv project
   - $ cd project
   - $ source bin/activate

- Now either run  install.sh or run the following manualy: 

- $ pip install "Django>=1.8"
- $ bin/django-admin.py startproject --template https://github.com/allox/django-base-template-1.8/zipball/master --extension py,md,rst mainapp
- $ mv mainapp/ src
- $ cd src
- Uncomment your preferred database adapter in requirements/compiled.txt (MySQL, Postgresql, or skip this step to stick with SQLite)
- $ pip install -r requirements/local.txt
- $ cp mainapp/settings/local-dist.py mainapp/settings/local.py
- $ chmod +x manage.py
- $ ./manage.py syncdb
- $ ./manage.py migrate
- $ ./manage.py collectstatic
- $ ./manage.py runserver





## Features ##

By default, this project template includes:

A set of basic templates and Twitter Bootstrap 3.3.5 (located in the
base app, with css and javascript included).

Templating:

- django_compressor for compressing javascript/css/less/sass

Authentication, registration
- allauth (+ base-template) 

Security:

- bleach
- bcrypt - uses bcrypt for password hashing by default

Background Tasks:

- Celery

Caching:

- python-memcached

Admin:

- Includes django-debug-toolbar for development and production (enabled for superusers)

Testing:

- nose and django-nose
- pylint, pep8, and coverage

Any of these options can added, modified, or removed as you like after creating your project.

## Python 3 compatability ##

All the code provided in the template itself is compatable with Python 3. Unfortunately, there are still a number of libraries that do not work under Python 3. If you want to use this template under Python 3, you will need to either remove those libraries or find replacements for them.

The libraries I am aware of that do not support Python 3:

* python-memcached (use python3-memcached)



## Prerequisites ##

- Python 2.6 or 2.7
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)



License
-------
This software is licensed under the [New BSD License][BSD]. 

[BSD]: http://opensource.org/licenses/BSD-3-Clause
