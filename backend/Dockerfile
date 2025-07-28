# syntax=docker/dockerfile:1
FROM python:3.13.5
WORKDIR /backend-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "app.py", "run"]