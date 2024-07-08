-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS properties;
DROP SEQUENCE IF EXISTS properties_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS properties_id_seq;
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    property VARCHAR(255),
    description VARCHAR,
    location VARCHAR,
    cost INTEGER
    user_id INTEGER
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, password) VALUES ('charlie_roberts23@hotmail.co.uk', 'Password!23');
INSERT INTO users (name, password) VALUES ('taconlin@hotmail.co.uk', 'Password!24');
INSERT INTO users (name, password) VALUES ('joshuadosanjh@gmail.com', 'Qwerty?09');

INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property1', 'This place is nice', 'test1', '999', '1');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property2', 'This place is okay', 'test2', '888', '1');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property3', 'This place is amazing', 'test3', '777', '2');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property4', 'This place is cool', 'test4', '666', '2');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property5', 'This place is wicked', 'test5', '555', '3');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property6', 'This place is rubbish', 'test6', '444', '3');
