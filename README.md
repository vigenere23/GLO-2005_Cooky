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
gunicorn app:app -b 127.0.0.1 -w 1 --log-level debug
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
