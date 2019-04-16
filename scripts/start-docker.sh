echo "Starting mysql docker..."
docker stop mysql1
docker rm mysql1
docker run -d \
--name mysql1 \
-p 3306:3306 \
--env "MYSQL_ROOT_PASSWORD=517ca3dd-35a8-4c4a-8449-ec9151a4cd14" \
mysql:8.0
docker start mysql1
echo "Done!"
