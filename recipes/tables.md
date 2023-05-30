# MakersBnB (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

## 1. Extract nouns from the user stories or specification

```
# USER STORIES:

Any signed-up user can list a new space.

Users can list multiple spaces.

Users should be able to name their space, provide a short description of the space, and a price per night.

Users should be able to offer a range of dates where their space is available.
```

```
Nouns:

user, space, name, description, price, dates
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| users                 | name, email, password
| spaces                | space_name, description, price, location, user_id
| bookings              | date, space_id, user_id

1. Name of the first table (always plural): `users` 

    Column names: `name`, `email`, `password`

2. Name of the second table (always plural): `spaces` 

    Column names: `space_name`, `description`, `price`, `location`, `user_id`

3. Name of the third table (always plural): `bookings` 

    Column names: `date`, `space_id`, `user_id`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```

Table: users
id: SERIAL
name: text
email: text
password: text

Table: spaces
id: SERIAL
space_name: text
description: text
price: float
location: text
user_id: int

Table: bookings
id: SERIAL
date: date
space_id: int
user_id: int
```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

```
1. Can one user have many spaces? YES
2. Can one user have many bookings? YES
3. Can one space have many bookings? YES
```

_If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case._

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `table1_table2`.


## 4. Write the SQL.

```sql
-- file: makersbnb.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    email text,
    password text
);

-- Create the second table.
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    description text,
    price float,
    location text,
    user_id int
);

-- Create the third table.
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date date,
    space_id int,
    user_id int
);

```

## 5. Create the tables.

```bash
psql -h 127.0.0.1 makersbnb < seeds/makersbnb.sql
```