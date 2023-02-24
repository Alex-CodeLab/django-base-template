
# Django4 / Django3 / Django2.2+ / Django1.11 complete installer #

## About ##


This template installs a fully functional Django website in just a few minutes.

Django 1.11 (for python2.7)
Django 2+ (python3)
includes bootstrap3, Allauth, and some other useful apps. These are easy to remove if you dont need it.

The goal of this template is to set up a fully functional django project in minutes, and have a clear project structure.

```
src                   # project root  
├── manage.py
├── /static
├── /config           # project configuration 
│   ├── /settings   
│   │   ├── base.py   # project settings   
│   │   ├── local.py  # local settings (development)
│   ├── urls.py        
│   ├── wsgi.py
├── /layout           # base templates and static files  
│   ├── models.py
│   ├── /staticu
    ... 
```






## Quick Install ##
first create a virtenv, activate. Then,  

```
source <(wget -qO- https://raw.githubusercontent.com/Alex-CodeLab/django-base-template/master/install.sh)
```
(if nothing happens when running above command, you should probably update ssl certs: `sudo update-ca-certificates --fresh && export SSL_CERT_DIR=/etc/ssl/certs` )


## Step by step Installation ##


- (when using python3) Make sure you have libevent-dev, python3-dev installed : 
```
$ sudo apt-get install libevent-dev python3-dev
```
- Install if not installed already :
```
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev libtiff5-dev libjpeg8-dev libffi-dev
```   
- Create your working environment and virtualenv:
```
$ virtualenv project
$ virtualenv -p python3 project  # for python3/django2
```
```    
$ cd project
$ source bin/activate
```
- run install.sh :
```
$ source <(wget -qO- https://raw.githubusercontent.com/Alex-CodeLab/django-base-template/master/install.sh)
```
  
...and that's all!



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

- Python  2.7 or 3.* 
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)



License
-------
This software is licensed under the [New BSD License][BSD]. 

[BSD]: http://opensource.org/licenses/BSD-3-Clause
