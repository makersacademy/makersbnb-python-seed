Two Tables (Many-to-Many) Design Recipe Template
Copy this recipe template to design and create two related database tables having a Many-to-Many relationship.

# 1. Extract nouns from the user stories or specification

Any signed-up user can list a new space.

Users can list multiple spaces.

Users should be able to name their space, provide a short description of the space, and a price per night.

Users should be able to offer a range of dates where their space is available.

Any signed-up user can request to hire any space for one night, and this should be approved by the user that owns that space.

Nights for which a space has already been booked should not be available for users to book that space.

Until a user has confirmed a booking request, that space can still be booked for that night.

Nouns:

user, space, desciption, price, dates, 

# 2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	| Properties
--------+-----------
user    |  name, email, password, bookings
space   |  name, description, price, dates_booked, dates_availible, user_id
bookings|  date, user_id, space_id, confirmed


Name of the first table (always plural): users

Column names: username, email, password, bookings

Name of the second table (always plural): spaces

Column names: description, price, dates_booked, dates_availible, user_id

3rd table: bookings

Column names: date, user_id, space_id


# 3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.


Table: users
id: SERIAL
username: text
email: text
password: text
bookings: int[]


Table: spaces
id: SERIAL
space_name: text
description: text
price: money
dates_booked: date[]
dates_available: date[]
user_id: int


Table: bookings
id: SERIAL
date: date
confirmed: bool
user_id: int
space_id: int 


# 4. Design relationship
Make sure you can answer YES to these two questions:

Can one user have many spaces? Yes (one item can be in many orders)

Can one space have many users? no

Can one space have many bookings? Yes

Can one user have many bookings? Yes


# 5. Write the SQL

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text,
    bookings int[]
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    description text,
    price money,
    user_id int, 
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date date,
    confirmed boolean
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade 
);



6. Create the tables
psql -h 127.0.0.1 bnb < seeds/bnb.sql