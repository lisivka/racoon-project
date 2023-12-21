Project name:
Backend internship at Mageap

Project description:

This project is an API application. The project is built using the Django REST Framework (DRF) for the API.

Development Tools:

    Python >= 3.11
    Django == 5.0
    Django REST Framework 3.14.0


Installation and running the project:

1) Clone the repository

       https://github.com/MaksymKashuba/Racoon-Project.git
2) Create a virtual environment

       cd Racoon-Project
       python -m venv venv

3) Activate virtual environment

   Linux

       source venv/bin/activate

   Windows

       ./venv/Scripts/activate
4) Install dependencies:

       pip install -r requirements.txt
5) In the root directory of the project, create an ".env" file. In the ".env" file, copy all the variables from the ".env.sample" file and give them values

7) Create migrations

       python manage.py makemigrations
8) Apply migrations to the database

       python manage.py migrate
9) Run server

       python manage.py runserver
10) Links

    DRF API 

        http://127.0.0.1:8000/
    DRF API Documentation

        http://127.0.0.1:8000/swagger/




License:

Copyright (c) 2023-present, internship Team
