# Department Project

[![Build Status](https://travis-ci.com/meg4ik/epam_final_project.svg?branch=main)](https://travis-ci.com/meg4ik/epam_final_project) [![Coverage Status](https://coveralls.io/repos/github/meg4ik/epam_final_project/badge.svg)](https://coveralls.io/github/meg4ik/epam_final_project)

## About Project
 Flask application for epam interview. Was made by Pavlo Ryndin.
 Functionality of the application can provide management groups of employees in company.

## Set Environment Variables


### Basics

1. Fork/Clone
1. Activate a virtualenv
1. Install the requirements


### Create DB

1. Install Mysql server
2. Create user:

```sh
$ CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'qwerty';
```

3. Assign privileges:

```sh
$ GRANT ALL PRIVILEGES ON *.* TO 'db_user'@'localhost';
```

4. Create database:

```sh
$ CREATE DATABASE department_project;
```

5. Create the tables and run the migrations:

```sh
$ flask db upgrade
$ python src/database/inserts.py
```

## Run the Application

```sh
$ python wsgi.py
```

You can change the startup config:

```sh
$ python wsgi.py --settings=configs.common_debug
```

```sh
$ python wsgi.py --settings=configs.common_deploy
```

Access the application at the address [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Testing

Testing with Pytest:

```sh
$ pytest
```

With more info:

```sh
$ pytest --cov=src tests/
```
