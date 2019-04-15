# App

## Database

### Preparing and executing

**Windows (on bash only)**:

```bash
./scripts/win-start-docker.sh
```

**Linux / Mac**

```bash
scripts/start-docker.sh
```

### Populating (on bash only)

```bash
./scripts/init-database.sh
```

## Server

### Preparing

```bash
cd app
pip3 install -r requirements.txt
```

### Executing

```bash
gunicorn app:app -b 0.0.0.0:5000 -w 1 --log-level debug
```

#### Without async support (NOT RECOMMENDED)

```bash
flask run
```

> WARNING : This methods will not work with the UI since it is based on multiple asynchroneous calls, which is not supported with the basic Flask server. 

## UI

### Peparing

```bash
cd ui
yarn install
```

> Note: This might take a while since some of the packages are quite huge. 

### Executing

```bash
cd ui
yarn serve
```

## Using Docker

With docker, the setup should be way easier, especially since it runs on Linux so it supports Gunicorn. All you have to do is running `docker-compose up` inside the root folder of the project. 

### Exposed ports

* MySQL DB : 32000
* Flask API : 8090
* VueJS UI : 8000

You can connect to those with localhost, 0.0.0.0, 127.0.0.1 or your docker-machine IP (depending or your OS).

### Connecting the UI

For now, only the server and the database are (successfully) connected inside the docker network. However, you can still use the UI like you normally would, outside the container. Just replace `yarn serve` by `yarn serve-docker` once the container is up. 