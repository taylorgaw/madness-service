#!/bin/bash
FROM python:3.8-slim-buster

ENV FLASK_APP=app.py
COPY api/requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENV PYTHONPATH=/api/

WORKDIR /api

ENTRYPOINT [ "python", "app.py" ]