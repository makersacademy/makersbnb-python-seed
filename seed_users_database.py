from lib.database_connection import DatabaseConnection

def seed_database(sql_file):
    db_connection = DatabaseConnection()
    db_connection.connect()
    for sql_file in sql_files:
        db_connection.seed(sql_file)

if __name__ == "__main__":
    sql_files = ["./seeds/spaces.sql", "./seeds/users.sql", "./seeds/bookings.sql"] 
    seed_database(sql_files)