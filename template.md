# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a User, I can sign up to the app.

As a signed up User, I can list new spaces including a name, short description and a price per night.

As a signed-up user, I can add a range of dates when a space is available.

As a signed-up user, I can request to book a space for one night.

As the space owner, I can approve a request to hire my space.

As a user, I should not be able to book nights for which a space is not available.

As a space owner, once I approve the request the space will not be available anymore.

```

```
Nouns:

User(email, username, password), spaces, name, description, price per night, Range of dates
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| User                  | Spaces          |
| --------------------- | ------------------|
| email                 | title
| first name            | description
| last name             | price
|  password             | range(list) of dates

1. Name of the first table (always plural): `users` 

    Column names: `email`, `first name`, `last name`, `password`

2. Name of the second table (always plural): `spaces` 

    Column names: `name`, `description`, `price`, `range(list) of dates`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
first name: text
last name: text
password: text

Table: spaces
id: SERIAL
title: text
description: text
price: money
range(list) of dates: date
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one user have many spaces? YES
2. Can one space have many users? NO

-> Therefore,
-> An user HAS MANY spaces
-> An space BELONGS TO an user

-> Therefore, the foreign key is on the spaces table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: spaces_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name text,
  email text,
  last_name text,
  password text
);

-- Then the table with the foreign key second.
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  title text,
  description text,
  price money,
  dates: date,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

```

## 5. Create the tables

```bash
psql -h 127.0.0.1 makersbnb-python < users_spaces.sql
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->