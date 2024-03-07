# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Booking:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def create_booking(self, property,date_from,date_to):
        # Parameters:
        #   create booking: a property and selected dates to book
        # Returns:
        #   Booking confirmed
        # Side-effects
        pass # No code here yet

    def show_user_bookings(self, user_id):
        # Returns:
        #   a list of bookings for a user id
        
        pass # No code here yet

    def show_property_bookings(self, property_name)
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a property and dates, a booking can be stored in the table
"""
def test_create_booking(db_connection):
    db_connection.seed("seeds/blueberries_b&b.sql")
    repository = BookingRepository(db_connection)

    repository.create_booking(Booking())

"""
When requested, all bookings for a user are shown
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
When requested, all bookings for a property are shown
"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
