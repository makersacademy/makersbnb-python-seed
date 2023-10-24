-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL,
    name text,
    description text,
    price int,
    date_from date,
    date_to date
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, description, price, date_from, date_to) VALUES ('Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01');
INSERT INTO spaces (name, description, price, date_from, date_to) VALUES ('Apartment 2', 'Description 2', 200, '2024-01-01', '2024-04-01');

