echo "Starting mysql docker..."
docker stop mysql1
docker run -d \
--name mysql1 --rm \
-p 1337:3306 \
--env "MYSQL_ALLOW_EMPTY_PASSWORD=yes" mysql:8.0
docker start mysql1
echo "Done!"