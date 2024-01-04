# Backend internship at Mageap

## Project description:

This project is an API application. The project is built using the Django REST Framework (DRF) for the API.

## Development Tools:

    Python >= 3.11
    Django == 5.0
    Django REST Framework 3.14.0

## Running the Project

1. **Prerequisites**

    - If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you
      can
      get python [here](https://www.python.org).
    - Docker should be installed on your computer. If it's not installed yet, refer to
      the [official Docker instructions](https://docs.docker.com/get-docker/).

2. **Environment Configuration**
    - Clone the repository
       [racoon-project](https://github.com/lisivka/racoon-project)
    - cd into your the cloned repo as such:
        ```
            cd Racoon-Project
        ```
    - Create and fire up your virtual environment:
        ```
            python -m venv venv
            venv\Scripts\activate
        ```
    - Create a `.env` file based on the `.env.example` template and fill in the required environment variables.
    - Install the dependencies needed to run the app:
        ```
            pip install -r requirements.txt
3. **Running with Docker Compose**
    - Open the terminal in the root directory of the project.
    - Run the command: `docker-compose up --build`.
    - After successful container startup, open a web browser and go to
      [DRF API](http://127.0.0.1:8000/), [DRF API Documentation](http://127.0.0.1:8000/swagger/)  to access the server.
4. **Stopping the Project**
    - To stop the project, press `Ctrl + C` in the terminal, then execute the command: `docker-compose down`.
> [!TIP]
> ## _Important Commands_
> - `docker-compose up --build`:  Initiates the project in development mode, building and starting all defined services.
> - `docker ps`: Lists currently running containers.
> - `docker ps -a`: Lists all containers, including both running and stopped ones.
> - `docker-compose down`: Halts and removes containers as defined in the Docker Compose file.
> - `docker system prune -a`: Clears unused Docker objects such as containers, volumes, networks, and images, freeing up
    disk space.
> - `docker-compose exec backend python manage.py [command]`: Runs Django commands within the backend container.
    Replace [command] with specific Django management commands like makemigrations, migrate, createsuperuser, etc.

> [!IMPORTANT]
> ## _Additional Information_
> #### When you start the project for the first time, use the command:
>> `docker-compose up --build`: Launch the project in development mode.`
> #### In the future, to launch the project, use the command:
>> `docker-compose up`
License:
Copyright (c) 2023-present, internship Team
> ---
>>  _old version_
> ---

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

       https://github.com/lisivka/racoon-Project.git
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



test data:

    python manage.py dumpdata > data.json

    python manage.py loaddata data.json

License:

Copyright (c) 2023-present, internship Team
