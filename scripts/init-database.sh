echo "Starting database initiation scripts"
echo "This might take a while..."
docker exec -i mysql1 mysql < bd_init/database.sql
docker exec -i mysql1 mysql < bd_init/tables.sql
# docker exec -i mysql1 mysql < bd_init/triggers.sql
docker exec -i mysql1 mysql < bd_init/inserts.sql
echo "Done!"