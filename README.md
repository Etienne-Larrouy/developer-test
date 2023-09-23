# Developer Technical Test

This project responds to the following developer test: [developer test](https://github.com/lioncowlionant/developer-test)

## Backend

### Requirements

Python 3.8+

### Install

To run the server, please install dependencies:

`pip3 install -r ./requirements.txt`

### Run dev

To run the server for dev, please execute the following from the root directory:

```bash
cd src/backend
python -m sanic odds_server:app --debug --reload
```

### Run prod

To run the server for prod, please execute the following from the root directory:

**Please consider that CORS issue can appear when running outside docker**

```bash
cd src/backend
python -m sanic odds_server:app
```
### Test

To launch the integration tests, use pytest:

`python -m pytest ./tests/`


### Running with Docker

#### Docker image build

To run the server on a Docker container, please execute the following from the root directory:

```bash
cd src/backend
# building the image
docker build -t odds_server .
```
#### Docker image build
```bash
cd src/backend
# starting up a container
docker run -d -p 8080:8080 odds_server
```

## Frontend

### Requirements

- Node 18.13.0 or newer

#### Install dependencies

`npm install`

#### Run dev

`npm run start`

#### Build

`npm run build`

## Docker

#### Build
```bash
cd src/frontend
# building the image
docker build . -t odds_app
```

#### Run
```bash
cd src/frontend
# starting up a container
docker run -d -p 8081:80 odds_app
```

## Acces

Access app to `http://localhost:8081`