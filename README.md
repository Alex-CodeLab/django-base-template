
# Django 1.8 Project Template - Bootstrap3, Allauth#

## About ##

This template is the result of many 'best practice' strategies for setting up a django project structure.
It aims to be simple, yet complete.

This version of the project template includes new options for Django 1.8 , has bootstrap3 installed and Allauth configured.

## Installation ##


- Make sure you have libffi installed 
   - $ sudo apt-get install libffi-dev
- (python3) Make sure you have libevent-dev, python3-dev  installed 
   - $ sudo apt-get install libevent-dev python3-dev
- Create your working environment and virtualenv:
   - $ virtualenv project

   python3:
   - $ virtualenv -p python3 project
    
   - $ cd project
   - $ source bin/activate

- Now either run  install.sh 
      - $ source <(wget -qO- https://raw.githubusercontent.com/allox/django-base-template-1.8/master/install.sh)
  
or run the following manually: 

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


* use python3-memcached instead of python-memcached



## Prerequisites ##

- Python 2.6 , 2.7 , 3 
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)



License
-------
This software is licensed under the [New BSD License][BSD]. 

[BSD]: http://opensource.org/licenses/BSD-3-Clause
