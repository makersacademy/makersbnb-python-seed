-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;


-- Then, we recreate them

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL,
    password text
);

-- Create the second table.
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    description text,
    price_per_night integer,
    availibility_start_date date,
    availibility_end_date date,
    owner_user_id integer,
    constraint fk_user FOREIGN KEY(owner_user_id) references users(id) on delete cascade
);


-- Create the third table
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id integer,
    booked_user_id integer,
    space_name text,
    date_booked date,
    status text,
    constraint fk_bookings_space_id FOREIGN KEY(space_id) references spaces(id) on delete cascade,
    constraint fk_bookings_user_id FOREIGN KEY(booked_user_id) references users(id) on delete cascade
    
);


INSERT INTO users(name,email,password) VALUES ('Test Name', 'testemail@mmm', 'pass');
INSERT INTO spaces(space_name, description,price_per_night,availibility_start_date,availibility_end_date, owner_user_id) 
VALUES ('Cornwall Beach Hut', 'Sunny hut on coast', 85, TO_DATE('01/06/23', 'DD/MM/YY'), TO_DATE('01/07/23', 'DD/MM/YY'), 1);

INSERT INTO spaces(space_name, description,price_per_night,availibility_start_date,availibility_end_date, owner_user_id) 
VALUES ('Norfolk Beach Hut', 'Sunny hut in North East', 85, TO_DATE('01/06/23', 'DD/MM/YY'), TO_DATE('01/07/23', 'DD/MM/YY'), 1);

INSERT INTO spaces(space_name, description,price_per_night,availibility_start_date,availibility_end_date, owner_user_id) 
VALUES ('Suffolk Beach Hut', 'Sunny hut in South', 85, TO_DATE('01/06/23', 'DD/MM/YY'), TO_DATE('01/07/23', 'DD/MM/YY'), 1);


INSERT INTO bookings(space_id, booked_user_id, space_name, date_booked, status) VALUES (1, 1, 'Sunny hut on coast', '01/06/23', 'Available');
INSERT INTO bookings(space_id, booked_user_id, space_name, date_booked, status) VALUES (2, 1, 'Sunny hut in North East', '02/06/23', 'Confirmed');
INSERT INTO bookings(space_id, booked_user_id, space_name, date_booked, status) VALUES (3, 1, 'Sunny hut in South', '03/06/23', 'Requested'); 