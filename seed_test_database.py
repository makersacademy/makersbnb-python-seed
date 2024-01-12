from lib.database_connection import DatabaseConnection

connection = DatabaseConnection(test_mode=True)
connection.connect()
connection.seed("seeds/makersbnb.sql")
