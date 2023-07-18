# Two Tables (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORIES:

```

```
Nouns:


```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                                  |
| --------------------- | --------------------------------------------|
| users                 | email, password.                            |
| properties            | name, description, price, user_id           |
| bookings              | start_date, end_date, user_id, property_id  |

1. Name of the first table (always plural): `users` 

    Column names: `email`, `password`

2. Name of the second table (always plural): `properties` 

    Column names: `name`, `description`, `price`, `user_id`

3. Name of the second table (always plural): `bookings`

    Column names: `start_date`, `end_date`, `user_id`, `property_id`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
email: text
password: text

Table: properties
id: SERIAL
name: text
description: text
price: numeric
user_id: int

Table: bookings
id: SERIAL
start_date: date
end_date: date
user_id: int
property_id

```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one user have many properties? (Yes)
2. Can one properties have many users? No

1. Can one user have many bookings Yes
2. Can one booking have many users No

1. Can one property have many bookings Yes
2. can one booking have many properties No

```
# EXAMPLE

1. Can one user have many ? YES

2. Can one post have many tags? YES
```
You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one user have many bookings YES
2. Can one booking have many users? NO

-> Therefore,
-> A user HAS MANY bookings
-> A booking BELONGS TO a user

-> Therefore, the foreign key is on the bookings table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  password text
);

-- Then the table with the foreign key second.
CREATE TABLE properties (
  id SERIAL PRIMARY KEY,
  name text,
  description VARCHAR(355),
  price numeric,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

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
```

## 5. Create the tables
