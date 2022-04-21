FROM python:3.9-alpine

RUN apk add make gcc musl-dev \
  && rm -rf /var/cache/apk/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

CMD python main.py