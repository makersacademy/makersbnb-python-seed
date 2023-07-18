# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: students

Columns:
id | name | cohort_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: properties

# Model class
# (in lib/property.py)
class Property


# Repository class
# (in lib/properties_repository.py)
class PropertyRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: 

# Model class
# (in lib/property.py)

class Property:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.description = ""
        self.price = 0
        self.user_id = 0

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: properties

# Repository class
# (in lib/property_repository.py)

class PropertyRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, description, price, user_id FROM property;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, description, price, user_id FROM property WHERE id = $1;

        # Returns a single property object.

        # Add more methods below for each operation you'd like to implement.

    def create(property)
        # Executes the SQL query:
        # INSERT INTO property (id, name, description, price, user_id) VALUES (%s, %s,%s,%s,%s)",[])


```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# Testing property class

    def test_property_constructor():
        property = Property(1,"NameTest1","DescriptionTest1",50.00,1)
        assert propery.id = 1
        assert propery.name = "NameTest1"
        assert propery.description = "DescriptionTest1"
        assert propery.price = 50.00
        assert propery.user_id = 1

    def test_compare_inputs_for_same_output():
        # given two same inputs it returns the same output

    def test_property_formatted_correctly():
        # when given a property object it returns a formatted string output


# Testing property_repository class

    def test_all_return_list_of_properties():
        # returns of properites from the seed database
    
    def test_create_property():
        # using the property class and returns #all method with
        # the new property class included

    def test_find_property():
        # finds a specific properties and returns the property object

    


# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._



