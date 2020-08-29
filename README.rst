CabShare
========

Cab share web application based on Django where a user can search and join other people having similar arrival/departure time.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Installation
------------
Make sure to have the following on your host:

- Python 3.8
- `PostgreSQL 12 <https://www.postgresql.org/download/windows/>`_
- Cookiecutter ``$ pip install cookiecutter``
- virtualenv ``$ pip install virtualenv``
 
Setup and the activate virtual environment ``$ virtualenv venv``

Install the dependencies in this venv (make sure that you are in the project folder)

- ``$ pip install -r requirements/base.txt``
- ``$ pip install -r requirements/local.txt``

Setup postgres database

- ``$ createdb cabshare -U postgres --password <password>``
- Go to config/settings/local.py and in DATABASES add your username and passowrd for postgres
Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy cabshare

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.

- ``$ python manage.py makemigrations``
- ``$ python manage.py migrate``
- ``$ python manage.py runserver``

Done!! The website is active on http://127.0.0.1:8000/



:Authors:
    Siddharth Jain,
    Anamitra Mandal

:Version: 0.1.0 of 29/08/2020
