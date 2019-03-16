# App

## Database

### Preparing

```bash
# Currently on the project's root directory
docker run -d \
--name mysql1 --rm \
-p 1337:3306 \
--volume %cd%/mysql:/docker-entrypoint-initdb.d/:ro \
--env "MYSQL_ALLOW_EMPTY_PASSWORD=yes" mysql:8.0
docker start mysql1
```

> Note: On Linux, the script `start-docker.sh` takes care of everything

### Populating

```bash
docker exec -i mysql1 mysql < bd_init/create_tables.sql
```

### Executing

```bash
docker exec -it mysql1 mysql
```

## Server

### Preparing

```bash
cd app
pip3 install -r requirements.txt
```

### Executing

```bash
cd app
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
