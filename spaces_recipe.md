Spaces Model and Repository Classes Design Recipe
Copy this recipe template to design and implement Model and Repository classes for a database table.

1. Design and create the Table
If the table is already created in the database, you can skip this step.

Otherwise, follow this recipe to design and create the SQL schema for your table.

In this template, we'll use an example table books


EXAMPLE
Table:  Columns: id | space_name | space_location | space_description | space_price | space_owner

2. Create Test SQL seeds
Your tests will depend on data stored in PostgreSQL to run. If seed data is provided (or you already created it), you can skip this step.

-- Write your SQL seed here. 
(file: seeds/makersbnb.sql)

DROP TABLE IF EXISTS makersbnb;
DROP TABLE IF EXISTS spaces;

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name VARCHAR(255),
    space_location VARCHAR(255),
    space_description VARCHAR(255),
    space_price INT,
    space_owner VARCHAR(255)
);

INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil');

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

psql -h 127.0.0.1 makersbnb_test < ~/Documents/Makers_Notes/group_project/makersbnb-python-seed/seeds/makersbnb.sql

#this creates the databse in the makersbnb_test database. Your route will be different!

3. Define the class names
Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

# Table name: space

# Model class
# (in lib/space.py)
class Space:


# Repository class
# (in lib/space_repository.py)
class SpaceRepository:


4. Implement the Model class
Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

# EXAMPLE
# Table name: space

# Model class
# (in lib/space.py)

'''class Spaces:
    def __init__(self, id, name, description, price, owner):
        id = int
        name = text
        location = text
        description = text
        price = int
        owner = text

    def __eq__(self, other):
        dictionary comparison

    def __repr__(self):
        format to string'''

class Spaces:
    def __init__(self, id, name, location, description, price, owner):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.price = price
        self.owner = owner

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Property name: {self.name}. /n
        location: {self.location}. /n
        Property Description: {self.description}. /n
        Price per night: £{self.price}. /n 
        Owner name and contact: {self.owner}."

# Implementation of values into the space object

    space_1 = Space(1, "Bob House", "Brighton", "3 bedrooms, 2 bathrooms, Victorian-era property", 300, "Bob")
    assert space_1.id == (1)
    assert space_1.name == ("Bob House")
    assert space_1.location == ("Brighton")
    assert space_1.description == ("3 bedrooms, 2 bathrooms, Victorian-era property")
    assert space_1.price == (300)
    assert space_1.owner == ("Bob")


You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.

5. Define the Repository Class interface
Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

# EXAMPLE
# Table name: spaces

# Repository class
# (in lib/space_repository.py)

"""class SpaceRepository:
    def __init__(self, connection):
        connectionn to database

    def all(self):
        connects to databse and runs SQL command to pull all data from spaces table         
        list of dictionaries"""
    
    def create(self, space)
        creates a new space in the database, ready to be booked

--as a next step (not as MVP) add search functions, e.g. find where location = '...'--

 #find b&b by location
    def find(self, spaces_location):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE location = %s', [spaces_location])
        row = rows[0]
        return Spaces(row["id"], row["name"], row["location"], row["description"], row["price"], row["owner"])

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(
                row['id'],
                row["name"], 
                row["location"], 
                row["description"], 
                row["price"],
                row["owner"])
            spaces.append(space)
        return spaces
    
    # Selecting all records
    # No arguments
    # Executes the SQL query:
    # SELECT id, name, location, description, price, owner FROM spaces;
    # Returns an array of space objects.
    

6. Write Test Examples
Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

"""
When space instance is created, 
it has id, name, location, description, price, owner 
"""
# Spaces Tests
def test_creates_space_instance():
    space = Spaces(1, "Bob House", "Brighton", "3 bedrooms, 2 bathrooms, Victorian-era property", 300, "Bob")
    assert space.id == 1
    assert space.name == "Bob House"
    assert space.location == "Brighton"
    assert space.description == "3 bedrooms, 2 bathrooms, Victorian-era property"
    assert space.price == 300
    assert space.owner == "Bob"

"""
Test to confirm equality of a record
"""
def test_record_is_equal():
    space_1 = Spaces('Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')
    space_2 = Spaces('Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')
    assert space_1 == space_2

    space_1 = Spaces(1, "Bob House", "Brighton", "3 bedrooms, 2 bathrooms, Victorian-era property", 300, "Bob")
    assert space_1.id == (1)
    assert space_1.name == ("Bob House")
    assert space_1.location == ("Brighton")
    assert space_1.description == ("3 bedrooms, 2 bathrooms, Victorian-era property")
    assert space_1.price == (300)
    assert space_1.owner == ("Bob")

"""
Tests that Space object is returned in
a nice format
"""
def test_formats_spaces_records_nicely():
    space = Spaces('Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')
    assert str(space) == "Property name: {self.name}. /n
        Property Description: {self.description}. /n
        Price per night: £{self.price}. /n 
        Owner name and contact: {self.owner}."

# Spaces repository tests
# 1
# Get all spaces

"""
When we call SpacesRepository#all
We get a list of spaces objects reflecting the seed data.
"""
def test_get_all_records_from_spaces(db_connection): 
    db_connection.seed("seeds/makersbnb.sql") 
    repository = SpaceRepository(db_connection)
    result = repository.all() # Get all spaces
    
    # Assert on the results
    assert result == [
        Spaces(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob');
        Spaces(2, 'Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim');
        Spaces(3, 'Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane');
        Spaces(4, 'Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan');
        Spaces(5, 'Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil')
    ]

# Database connection test
"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/database_connection.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM test_table")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "name": "first_record"},
        {"id": 2, "name": "second_record"}
    ]
Encode this example as a test.

7. Test-drive and implement the Repository class behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.