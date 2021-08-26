FROM python:3.9-slim-buster

COPY requirements.txt /usr/app/requirements.txt

RUN pip install -r /usr/app/requirements.txt

COPY . /usr/app

WORKDIR /usr/app

EXPOSE 5000

CMD ["python", "app.py"]

