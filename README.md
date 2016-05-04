utvsapi-django
==============

A REST-like read-only API for [ÚTVS ČVUT](https://rozvoj.fit.cvut.cz/Main/rozvrhy-utvs-db)
implemented in [Django REST framework](http://www.django-rest-framework.org/).

To use this, create file named `mysql.cnf` with your MySQL credentials, see an example here:

    [client]
    host = localhost
    user = username
    database = dbname
    password = insecurepassword

This has been developed and run on Python 3 only, legacy Python might not work.

Install depnedncies (you'll need mysql devel package for that). You might do it with virtualenv:

    pyvenv venv
    . venv/bin/activate
    pip install Django==1.9 django-filter djangorestframework drf-hal-json mysqlclient utvsapitoken

Start the service in debug mode:

    python3 ./manage.py runserver

Or run with gunicorn:

    pip install gunicorn
    gunicorn utvsapi.wsgi

License
-------

This software is licensed under the terms of the MIT license, see LICENSE for full text and copyright information.
