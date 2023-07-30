# demo-python-flask-postgres
Simple PoC using Flask, Postgres and SQLAlchemy

## How to install
Run in the project root directory

```shell
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## How to run
While on virtualenv

```shell
$ flask run
```

With gunicorn:

```shell
pip install gunicorn
gunicorn 'app:app'
```

## Environment variables

```
POSTGRES_HOST=???
POSTGRES_DATABASE=???
POSTGRES_USERNAME=???
POSTGRES_PASSWORD=???
# for flask
FLASK_RUN_PORT=???
# for gunicorn
PORT=???
```
