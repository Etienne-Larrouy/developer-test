FROM python:3.10.6-alpine
WORKDIR /usr/src/app
COPY . .

RUN pip3 install -vvv --no-cache-dir --user -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sanic"]
CMD ["src.backend.odds_server:app"]
