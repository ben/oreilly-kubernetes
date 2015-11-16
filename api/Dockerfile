FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["gunicorn", "api.server:app"]
