Two Tables Design Recipe Template
1. List all the nouns.
2. Decide whether a noun is a record (a table name) or a property of it (a column).
3. Decide the column types.
4. Decide how the two tables will be related (where the foreign key is needed).
5. Write the SQL to create the tables.

## 1. Extract nouns from the user stories or specification
```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

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


```

```
Nouns: user, username, password, space, spaces, status, price, description, dates, booking request, approval, night
```
Verbs: login, register, authorise, list, manage, refuse, book, confirm, check status

## 2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

| 🍒 BnB 🍒   | Properties                                                                          |
|------------|-------------------------------------------------------------------------------------|
| User       | username, password, list of spaces,                                                 |
| Space      | name, desciption, price, user_id (foreign key)                                      |
| Booking    | date, status, space_id (foreign key), guest_id (foreign key)                        |



1. Name of the first table (always plural): `users` 
   Column names: `user_name`, `user_password`, `user_spaces`
2. Name of the second table (always plural): `spaces` 
   Column names: `space_name`, `description`, `price_per_night`, `user_id`, `availability`, `status`


## 3. Decide the column types
[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.
```
# EXAMPLE:

Table: users
id: SERIAL
user_name: TEXT
user_password: TEXT
user_spaces: ?

Table: spaces
id: SERIAL
space_name: TEXT
description: TEXT
price_per_night: NUMERIC
user_id: INT

Table: bookings
id: SERIAL
date: DATE
status: BOOLEAN
space_id: INT
guest_id: INT

```

## 4. Decide on The Tables’ Relationship
Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:
1. Can one user have many space? Yes
2. Can one space have many users? No

You'll then be able to say that:
1. **users have many spaces**
2. And on the other side, **space belongs to user**
3. In that case, the foreign key is in the table 'spaces'

```

```

## 5. Write the SQL
```sql
-- file: albums_table.sql
-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  user_name text,
  user_password text,
);

-- Then the table with the foreign key second.
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  price_per_night numeric,
  user_id int
-- The foreign key name is always {other_table_singular}_id
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  date date,
  status boolean,
  space_id int,
  guest_id int
-- The foreign key name is always {other_table_singular}_id
  constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade
  constraint fk_guest foreign key(guest_id)
    references users(id)
    on delete cascade
);
```

## 6. Create the tables
```bash
psql -h 127.0.0.1 cherry_b_n_b < bnb_table.sql
```

