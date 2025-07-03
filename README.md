# cct-devops-diploma-2025-template
Template to kickstart your DevOps Diploma 2025 Project

# Starting the server

## Create a virtual environment

First you need to create and activate a [Python Virtual Environment](https://docs.python.org/3/library/venv.html)

```bash
$ python -m venv ./.venv
$ source ./.venv/bin/activate
```

## Install the dependencies

There's a file in this project named `requirements.txt` this is a common file found in python project and it contains a list of all dependencies needed to run it

```bash
$ pip install -r requirements.txt
```

## Run the Server

You should now be able to start the server

```bash
$ python manage.py runserver
```