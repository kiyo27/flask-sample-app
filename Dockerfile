FROM python:3.9.6

RUN pip install Flask flask-restx

WORKDIR /app