-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(255),
  email_address VARCHAR(255),
  passcode VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  price INTEGER,``
  user_id INTEGER
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (fullname, email_address, passcode) VALUES ('Peter Pan', 'peterpan', 'peter&1234');
INSERT INTO users (fullname, email_address, passcode) VALUES ('Jenny Mill', 'notsoFar', 'docker&1234');
INSERT INTO users (fullname, email_address, passcode) VALUES ('kevin Tosh', 'kevin-90', 'linux456789!');

INSERT INTO users (name, descr, price, user_id) VALUES ('Yellow', '', '', 0);
