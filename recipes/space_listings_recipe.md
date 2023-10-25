# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
As a user I want to visit a website to view spaces.
As a user so that I can book a space, I want to see the name of the space, a description of it, date it is available, and the price.


```

```
Nouns:

spaces, date, description, price, name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| spaces                | name, description, price, date from, date to
|                 | 

1. Name of the first table (always plural): `spaces` 

    Column names: `name`, `description`, `price`, `date from`, `date to`

<!-- 2. Name of the second table (always plural): `comments` 

    Column names: `content`, `name` -->

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
price: int
date from: date
date to: date


```

<!-- ## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one user have many [spaces? Yes
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one post have many comments? YES
2. Can one comment have many posts? NO

-> Therefore,
-> An post HAS MANY comments
-> An comments BELONGS TO a post

-> Therefore, the foreign key is on the comments table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).* -->

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: posts_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE spaces (
    id: SERIAL
    name: text
    description: text
    price: int
    date from: date
    date to: date
);



-- -- Then the table with the foreign key second.
-- CREATE TABLE comments (
--   id SERIAL PRIMARY KEY,
--   content text,
--   name text,
-- -- The foreign key name is always {other_table_singular}_id
--   post_id int,
--   constraint fk_post foreign key(post_id)
--     references posts(id)
--     on delete cascade
-- );

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 bnb_legends < spaces.sql

```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_table_design_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->