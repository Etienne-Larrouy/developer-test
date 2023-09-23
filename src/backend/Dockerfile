FROM python:3.10.6-alpine
WORKDIR /usr/src/backend
COPY . .

RUN pip3 install --no-cache-dir --user -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["-m", "sanic", "odds_server:app", "--port=8080", "--host=0.0.0.0"]
