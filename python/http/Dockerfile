FROM python:3.7-alpine

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "gunicorn.conf", "invoker:app"]