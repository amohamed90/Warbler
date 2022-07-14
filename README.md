# Warbler
A Twitter clone with a cooler bird.

![Screenshot of Warbler sign-in page](static/images/warbler-home.png)

## Getting Started
Follow the instructions below to get a copy of the project up and running on your machine for development and testing. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- Python 3.6 or higher
- PostgreSQL
- The following databases
  - warbler (for dev)
  - warbler-test (for testing)

### Installing
1. Clone the repo
2. Create a venv (virtual environment) for the app by doing the following:
```
$ python3 -m venv venv
$ source ./venv/bin/activate
```
3. Install the packages in requirements.txt with:
```
$ pip install -r requirements.txt
```
4. Create the _warbler_ and _warbler-test_ databases in PostgreSQL and load data:

- Dev database and data:
```
$ createdb warbler
$ psql warbler < data.sql

```
- Test database and data:
```
$ createdb warbler-test
$ psql warbler-test < data.sql
```
5. Start the server:
```
$ flask run
```

### Running Tests
All tests: `python -m unittest`

Specific test: `python -m unittest [testfile-name.js]`

## Built With
- [Python](https://www.python.org/) - language for server
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - web app framework
- [Jinja2](https://palletsprojects.com/p/jinja/) - HTML templating language for Python
- [bcrypt](https://pypi.org/project/bcrypt/) - password hashing
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - extension for Flask to support SQLA ORM
- [psycopog2](https://pypi.org/project/psycopg2/) - PostgreSQL adapter for Python
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - form validation and rendering library for Python with Flask integration
