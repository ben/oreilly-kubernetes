FROM python:3

EXPOSE 8000
WORKDIR /app
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "api.server:app"]

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
