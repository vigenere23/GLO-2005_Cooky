echo "Starting database initiation scripts. This might take a while..."

echo "1/7  Creating database..."
docker exec -i mysql1 mysql < bd_init/1_database.sql

echo "2/7  Defining tables..."
docker exec -i mysql1 mysql < bd_init/2_tables.sql

echo "3/7  Adding constraints..."
docker exec -i mysql1 mysql < bd_init/3_constraints.sql

echo "4/7  Creating procedures..."
docker exec -i mysql1 mysql < bd_init/4_procedures.sql

echo "5/7  Creating triggers..."
docker exec -i mysql1 mysql < bd_init/5_triggers.sql

echo "6/7  Filling static tables..."
docker exec -i mysql1 mysql < bd_init/6_populate_static.sql

echo "7/7  Filling other tables...(longer)"
python fill_db.py

echo "Done!"
