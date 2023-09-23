# Developer Technical Test

This project responds to the following developer test: [developer test](https://github.com/lioncowlionant/developer-test)

## Backend

### Requirements

Python 3.8+

### Install

To run the server, please install dependencies:

```bash
pip3 install -r ./src/backend/requirements.txt
```

### Run dev

To run the server for dev, please execute the following from the root directory:

```bash
python -m sanic src.backend.odds_server:app --debug --reload
```

### Run prod

To run the server for prod, please execute the following from the root directory:

```bash
python -m sanic src.backend.odds_server:app
```
### Test

To launch the integration tests, use pytest:

```bash
python -m pytest ./src/backend/tests/
```

### Running with Docker

#### Docker image

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t odds_server .

# starting up a container
docker run -p 8080:8080 odds_server
```