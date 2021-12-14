# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /api
ENV FLASK_APP=utils/app.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]