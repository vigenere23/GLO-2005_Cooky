FROM python

WORKDIR /

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /

EXPOSE 8080

CMD ["flask", "run"]
