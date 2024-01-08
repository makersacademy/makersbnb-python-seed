As a user I would like to be able to list multiple spaces.

As a user
so that I can make my advertised space more appealing
I need to be able to add a short description and price

As a user
so that I can advertise on different days
I need to be able to specify a range of dates where the space is available


--- ROUTE LAYOUT ---
/Spaces GET method
List the available spaces and the associated details.
Select all data from the ListSpaces database arrange in reverse chrono order(newest first) display to the user.
execute 'SELECT * FROM Spaces' 

--- NOUNS ---
user, spaces, title, description, price, daterange


--- TABLE LAYOUT ---

RECORD | PROPERTIES

Spaces | title, description, price, daterange, user_id

--- DATA TYPES ---

Spaces:
    * id: SERIAL
    * title: text
    * description: text
    * price: float
    * daterange: text
    * user_id: int

seed data located in Spaces.sql and SpacesTest.sql

--- CLASS BREAKDOWN ---

Space - Model Class No functions. Just holds data.

SpacesRepository - Repository Class

    * __init__: establish database connection
    * list_all(): Takes no arguments. Returns list of Space objects. Executes Select * FROM Spaces
    




