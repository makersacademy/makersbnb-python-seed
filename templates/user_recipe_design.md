## 1. Describe the Problem

As a User,
I want to be able to create an account
with a username and password

As a User,
I want to be able to login
with my username and password

As a User,
I want to be able to add a new space with the following properties:
1. Name
2. Price per night
3. Description
4. Range of dates
5. Availablility
6. Confrimed rentals

As a User,
I should see all available spaces from all Users

As a User,
I should be able to request to rent a space for a specific date

As a User,
I should be able to check the status of my request

As a User,
I should be able to authorise or refuse a request for space/date


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class User:
    # User-facing properties:
    #   username: string
    #   password: string

    def __init__(self, username, password):
        # Parameters:
        #   username: string
        #   password: string
        self.username = username
        self.password = password
        self.spaces = []

    def add_space(self, name, description, price_per_night):
        # Parameters:
        #   name: string
        #   descripton: string
        #   price_per_night: numeric
        #   
        # Returns:
        #   Nothing. Creates a new space in database
        #   Or returns list of spaces that has been added??
        pass # No code here yet

    def view_spaces(self):
        # Returns:
        #   A list of all the spaces from database
        pass # No code here yet

    def request_rental(self, space_id, date):
        # Parameters:
        #   space_id: int
        #   date: Date
        # Returns:
        #   Nothing. Creates a booking request in database for that specific date
        pass # No code here yet

    def check_status(self, booking_id):
        # Parameters:
        #   booking_id: int
        # Returns:
        #   Returns the current status of the booking
        pass # No code here yet

    def respond(self, booking_id, respond):
        # Parameters:
        #   booking_id: int
        #   response: string
        # Returns:
        #   Updates the status of booking in database based on the respond
        pass # No code here yet

```
#initialise list of users also?
#status when adding a space?
#returns list of spaces that we added? when adding
#what about valid or invalid email and password?

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python


"""
Given there is no spaces. View spaces returns empty list.
"""
def test_when_empty_list_of_spaces():
    user = User('Adamexample@gmail.com', 'password1234!')
    assert user.view_spaces() == []


"""
User adds a new space and then list all the spaces. User can see that space has been added.
"""
def test_when_one_space_added():
    user = User('Adam.takac@gmail.com', 'password456!')
    user.add_space('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)
    assert user.view_spaces == ('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)

"""
User adds multiple spaces and then lists all the spaces. User can see all the added spaces.
"""
def test_when_multiple_spaces_added():
    user = User('adamtakac24@outlook.com', 'Password$123')
    user.add_space('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)
    user.add_space('Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00)
    user.add_space('Lake District treehouse', 'Adventorous treehouse cabin located in Lake District.', 100.00)
    assert len(user.view_spaces()) == 3
    assert user.view_spaces == [
        {'name': 'Cozy Cottage', 'description': 'A charming cottage in the countryside.', 'price_per_night': 120.00},
        ['name': 'Luxurious apartment', 'description': 'Stunning luxurious apartment in the city center.', 'price_per_night': 250.00]
        ['name': 'Lake District treehouse', 'description': 'Adventorous treehouse cabin located in Lake District.','price_per_night': 100.00]
    ]






## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
