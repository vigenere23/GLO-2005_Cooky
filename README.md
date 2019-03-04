# App

## Initialization

### Server

```bash
pip3 install -r requirements.txt
```

### Database

```bash
docker run -d \
--name mysql1 \
--volume <PROJECT_PATH>/mysql:/var/lib/mysql \
--env "MYSQL_ALLOW_EMPTY_PASSWORD=yes" mysql
docker start mysql1
docker exec -i mysql1 mysql < bd_init/create_tables.sql
```

Where `<PROJECT_PATH>` should be the **absolute** path to the project's root directory. 

### UI

...todo

## Execution

### Server

```bash
flask run
```

### Database

```bash
docker exec -it mysql1 mysql
```

### UI

...todo
