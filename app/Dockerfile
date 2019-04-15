FROM python

WORKDIR /

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5000", "--workers=1", "--log-level=debug", "--timeout=60", "--env", "DB_HOST=db", "--env", "DB_PORT=3306"]
# CMD ["flask", "run"]
