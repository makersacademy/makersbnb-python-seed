-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS spaces;

-- Then, we recreate them
CREATE TABLE spaces (id SERIAL PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), price INT);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, description, price) VALUES ('Name1', 'Description of space', 20);
INSERT INTO spaces (name, description, price) VALUES ('Name2', 'Another description of space', 30);