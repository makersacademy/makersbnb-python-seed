from lib.database_connection import DatabaseConnection

# Run this file to reset your database using the seeds
# ; pipenv run python seed_dev_database.py
#
# comment the next line to set: DEBUG MODE OFF   (change in conftest.py too!!!)
test_mode = False
#######
connection = DatabaseConnection(test_mode)
connection.connect()
connection.seed("seeds/makersbnb_db_data.sql")
# Add your own seed lines below...
# E.g.connection.seed("seeds/your_seed.sql")
