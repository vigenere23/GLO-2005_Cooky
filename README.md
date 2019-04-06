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
flask run
```

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
