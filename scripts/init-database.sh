echo "Starting database initiation scripts. This might take a while..."

echo "1/5  Creating database..."
docker exec -i mysql1 mysql < bd_init/database.sql

echo "2/5  Creating tables..."
docker exec -i mysql1 mysql < bd_init/tables.sql

echo "3/5  Creating triggers..."
docker exec -i mysql1 mysql < bd_init/triggers.sql

echo "4/5  Filling static tables..."
docker exec -i mysql1 mysql < bd_init/populate_static.sql

echo "5/5  Filling other tables..."
python3 fill_db.py

echo "Done!"