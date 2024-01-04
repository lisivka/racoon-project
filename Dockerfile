# pull official base image
FROM python:3.11-alpine

MAINTAINER Vitalii

# set work directory
RUN mkdir /drf_app
WORKDIR /drf_app

# set environment variables
ENV PYTHONUNBUFFERED=1


RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
COPY start.sh .
# Expose port
EXPOSE ${APP_PORT}

RUN chmod +x start.sh

# entrypoint to run the django.sh file
ENTRYPOINT ["sh", "/drf_app/start.sh"]