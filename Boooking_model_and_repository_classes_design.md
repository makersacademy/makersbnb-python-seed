# Booking Model and Repository Classes Design

## 1. Design and create the Table


Table: bookings

Columns:
id | start_date | end_date | user_id | property_id


## 2. Create Test SQL seeds

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  start_date date,
  end_date date,
-- The foreign key name is always {other_table_singular}_id
  property_id int,
  constraint fk_property foreign key(property_id)
    references properties(id)
    on delete cascade,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-01-01', '2024-01-08', 1, 4);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-02-14', '2024-02-15', 2, 2);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-06-07', '2024-08-07', 3, 1);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-01-10', '2024-01-16', 1, 3);


## 3. Define the class names


```python
# Table name: bookings

# Model class
# (in lib/booking.py)
class Booking


# Repository class
# (in lib/booking_repository.py)
class BookingtRepository

```

## 4. Implement the Model class

```python
# EXAMPLE
# Table name: bookings

# Model class
# (in lib/booking.py)

class Booking:
    def __init__(self, id, start_date, end_date, property_id, user_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.property_id = property_id
        self.user_id = user_id

#tests
'''
booking constructs with an id, start_date, end_date, user_id, property_id
'''
# We can format bookings nicely
# We can compare 2 identical bookings
# We can assess a booking for validity
# We can generate errors for invalid bookings


## 5. Define the Repository Class interface

```python
# 
# Table name: bookings

# Repository class
# (in lib/booking_repository.py)

class BookingRepository:

    def all():
        # Selecting all records
        # No arguments
        # Executes the SQL query:
        # SELECT id, start_date, end_date, property_id, user_id FROM bookings;

        ### Returns an array of Booking objects. ###

    def find(id):
        # Gets a single record by its ID
        # One argument: the id (number)
        # Executes the SQL query:
        # SELECT id, name, start_date, end_date, property_id, user_id WHERE id = $1;

        ## Returns a single Booking object. ##


     def create(booking):
        # Creates a new record
        # One argument: the booking object(id=None)
        # executes the SQL query:
        '''INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES (%s,%s,%s,%s,) RETURNING id
        '''

        ## Returns the Booking object with the id that was assinged automatically. ##


```

## 6. Write Test Examples

```python
# EXAMPLES

# 1
# Get all bookings
repo = BookingRepository()
bookings = repo.all()
len(bookings) # =>  4
bookings # =>  [
    Booking(1,'2024-01-01', '2024-01-08', 1, 4),
    Booking(2,'2024-02-14', '2024-02-15', 2, 2),
    Booking(3,'2024-06-07', '2024-08-07', 3, 1),
    Booking(4,'2024-01-10', '2024-01-16', 1, 3)
]
 
# 2
# Get a single booking
repo = BookingRepository()
bookings = repo.find(3)
booking.id # =>  3
booking.start_date # =>  '2024-06-07'
booking.end_date # =>  '2024-08-07'
booking.user_id # =>  3
booking.property_id # =>  1

#3
# Create a new booking, get back that booking and have it reflected when we call #all
repo = BookingRepository()
repo.create(None,'2023-05-30', '2023-09-15',3,2) #=> Booking(5,'2023-05-30', '2023-09-15', 3, 2)
bookings = repo.all()
bookings # =>  [
    Booking(1,'2024-01-01', '2024-01-08', 1, 4),
    Booking(2,'2024-02-14', '2024-02-15', 2, 2),
    Booking(3,'2024-06-07', '2024-08-07', 3, 1),
    Booking(4,'2024-01-10', '2024-01-16', 1, 3),
    Booking(5,'2023-05-30', '2023-09-15', 3, 2)
]