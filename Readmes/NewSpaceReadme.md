As a user I would like to be able to list a space on the website.

As a user I would like to be able to list multiple spaces.

As a user
so that I can make my advertised space more appealing
I need to be able to add a short description and price

As a user
so that I can advertise on different days
I need to be able to specify a range of dates where the space is available

--- ROUTE LAYOUT ---

/newspace GET method
Load input form for the user to start their new listing

/newspace POST method
Take input data and add it to the database
executes INSERT INTO Spaces (attr) VALUES (vals)

Using Spaces table layout from list pages and sql from list pages. (see ListSpacesReadme.md)

Using classes from ListSpaces

---CLASS AMENDMENT ---

SpacesRespository

    * add() : Take title,space_description,price,daterange,user_id. Create new listing in Spaces table for later viewing. Executes INSERT INTO Spaces (attr) VALUES (vals). Return nothing. Side effects: Adds new listing to table.