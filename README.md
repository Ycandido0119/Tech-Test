# Tech-Test

## Application

This is a Django web application for storing files.

## Setup

The commands are all based on if you are on a Mac. The first step in terms of setting up this repo is to set up your virtual environment.

```bash
source mysite/bin/activate
```

## Installation

Packages to install:

Before you setup the virtual environment you need to check if you have installed python. If you haven't installed python you can download from here: https://www.python.org/

```bash
python --version
```

If python is installed you will recieve a response in the form of a version number, like this:

```bash
Python 3.11.5
```

Once you have setup your virtual environment you will need to install Django. Before doing so you must use a package manaager like PIP, to check if your system has PIP installed, run this command in the command prompt:

```bash
pip --version
```

If PIP is installed, you will get a result the version number. Which will look like this:

```bash
pip 23.2.1 from /Users/yassircandido/Tech-Test/mysite/lib/python3.11/site-packages/pip (python 3.11)
```

Now you can install Django using pip, with this command:

```bash
python -m pip install django 
```

To check if Django is installed by asking for its version number like this:

```bash
django-admin --version
```
If Django is installed, you will get this result:

```bash
4.2.5
```
## Start up

How to get it running?

When running the Django project make sure you are in the local environment. Navigate to the project's folder "octoapp" and execute this command in the command prompt:

```bash
cd octoapp
python manage.py runserver
```
Now you need to import the files into the datab

To get into the admin site once you have ran that command enter the browser window, add the admin url in the address bar.

To log in to the admin application, you need to create a user. This is done by typing this command in the command view:

```bash
python manage.py createsuperuser
```

After you must enter: username, email address and a password.  