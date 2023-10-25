-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
-- added cascade as was getting an error that cannot get drop table as it depends on other table
DROP TABLE IF EXISTS users cascade; 
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    name text,
    email text,
    password text

);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, name, email, password) VALUES ('username1', 'name1', 'email1', 'password1');
INSERT INTO users (username, name, email, password) VALUES ('username2', 'name2', 'email2', 'password2');

DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int,
    date_from date,
    date_to date,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, description, price, date_from, date_to, user_id) VALUES ('Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01', 1); 
INSERT INTO spaces (name, description, price, date_from, date_to, user_id) VALUES ('Apartment 2', 'Description 2', 200, '2024-01-01', '2024-04-01', 2);
