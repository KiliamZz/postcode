FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN  pip install -r requirements.txt

ENTRYPOINT python main.py