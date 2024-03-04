-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    password VARCHAR(255)

);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price float,
-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);





-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email_address, password) VALUES ('user_1@test.com', 'Rock');
INSERT INTO users (email_address, password) VALUES ('user_2@test.com', 'Pop');
INSERT INTO users (email_address, password) VALUES ('user_3@test.com', 'Pop');
INSERT INTO users (email_address, password) VALUES ('user_4@test.com', 'Jazz');



-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, description, price, user_id) VALUES ('space_1', 'description_1', 45.50, 1);
INSERT INTO spaces (name, description, price, user_id) VALUES ('space_2', 'description_2', 14000.99, 2);    



