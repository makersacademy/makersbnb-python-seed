# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a user so I can create a space 
I  need to add the name, the description and the price per night

As a user 
I want to keep a list of my listed spaces

As user so that I can have an overview of the available spaces
I want to see a list of available spaces with their names, description and price per night

As a user so I can select a space 
I need to see the page dedicated to a specific space



```
Nouns:

user space, space_name, description, price
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| space                 | space_name, description, price
| user                  | username

1. Name of the first table (always plural): `spaces` 

    Column names: `name`, `description`, 'price'

2. Name of the second table (always plural): `artists` 

    Column names: `users`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: spaces
id: SERIAL
name: text
description: text
price: numeric

Table: users
id: SERIAL

```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one user have many spaces? YES
2. Can one space have many users? NO

You'll then be able to say that:

1. **A user  has many [B]spaces**
2. And on the other side, **[B]a space belongs to user[A]**
3. In that case, the foreign key is in the table [B] - spaces (user_id)

Replace the relevant bits in this example with your own:

```

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text

);

-- Then the table with the foreign key second.
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  price decimal (7, 2)
-- The foreign key name is always {other_table_singular}_id
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```