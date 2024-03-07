-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS booking_requests;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP SEQUENCE IF EXISTS booking_requests_id_seq;

-- Then we recreating the sequences
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  user_name text,
  user_password text
);


CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  price_per_night numeric,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  date date,
  status text,
  space_id int,
  guest_id int,
-- The foreign key name is always {other_table_singular}_id
  constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade,
  constraint fk_guest foreign key(guest_id)
    references users(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS booking_requests_id_seq;
CREATE TABLE booking_requests (
  id SERIAL PRIMARY KEY,
  booking_id int,
  request_status VARCHAR(10) NOT NULL CHECK (request_status IN ('confirmed', 'declined', 'pending')),
  constraint fk_booking foreign key(booking_id)
    references bookings(id)
    on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
-- Inserting data into the 'users' table
INSERT INTO users (user_name, user_password) VALUES ('Adamexample@gmail.com', 'password123!!!');
INSERT INTO users (user_name, user_password) VALUES ('adam.takac24@outlook.com', 'password456!!!');

-- Inserting data into the 'spaces' table
INSERT INTO spaces (name, description, price_per_night, user_id) VALUES ('Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1);
INSERT INTO spaces (name, description, price_per_night, user_id) VALUES ('Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00, 2);

-- Inserting data into the 'bookings' table
INSERT INTO bookings (date, status, space_id, guest_id) VALUES ('2024-07-13', True, 1, 2);
INSERT INTO bookings (date, status, space_id, guest_id) VALUES ('2024-06-25', False, 2, 1);

-- Inserting data into the 'booking_request' table
INSERT INTO booking_requests (booking_id, request_status) VALUES (1, 'pending');
INSERT INTO booking_requests (booking_id, request_status) VALUES (2, 'confirmed');