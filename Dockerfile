FROM python:3.6-alpine

RUN adduser -D itp4924-homework-a04

WORKDIR /home/itp4924-homework-A04

COPY requirements.txt requirements.txt
RUN apk add --no-cache --update gcc musl-dev libffi-dev openssl-dev
RUN python3 -m venv venv
RUN venv/bin/pip3 install --upgrade pip
RUN venv/bin/pip3 install -r requirements.txt
RUN venv/bin/pip3 install gunicorn

COPY app app
COPY migrations migrations
COPY config.py run.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

RUN chown -R itp4924-homework-a04:itp4924-homework-a04 ./
USER itp4924-homework-a04

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
