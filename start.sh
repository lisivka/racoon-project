#!/bin/bash

wait_for_postgres() {
    until nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
        echo "PostgresSQL is not available. Waiting..."
        sleep 2
    done
    echo "PostgresSQL started"
}

wait_for_postgres
echo "PostgreSQL is ready. Proceed with your script."

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --no-input
python manage.py loaddata data.json


echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000

# end of file

