echo "Starting mysql docker..."
docker stop mysql1
docker run -d \
--name mysql1 \
-p 3306:3306 \
--volume "$PWD/mysql":/docker-entrypoint-initdb.d/:ro \
--env "MYSQL_ALLOW_EMPTY_PASSWORD=yes" mysql
docker start mysql1
echo "Done!"
