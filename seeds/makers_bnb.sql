-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS availability;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;

-- Then, we recreate them
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    telephone_number VARCHAR(255),
    password VARCHAR(50));

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    user_id int,
    name VARCHAR(255),
    description VARCHAR (500),
    price_per_night int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

CREATE TABLE availability (
    id SERIAL NOT NULL UNIQUE,
    space_id int,
    date date,
    status boolean,
    primary key (space_id, date),
    constraint fk_space foreign key(space_id) references spaces(id) on delete cascade
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    night_id int,
    user_id int,
    status VARCHAR (9),
    constraint fk_night foreign key(night_id) references availability(id) on delete cascade,
    constraint fk_user foreign key (user_id) references users(id) on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (first_name, last_name, email, telephone_number, password) VALUES ('Alex', 'Adams', 'email1@email.com', '01234567891', 'password1');
INSERT INTO users (first_name, last_name, email, telephone_number, password) VALUES ('Charlie', 'Smith', 'email2@email.com', '01234567892', 'password2');
INSERT INTO users (first_name, last_name, email, telephone_number, password) VALUES ('Jamie', 'Brown', 'email3@email.com', '01234567893', 'password3');

INSERT INTO spaces (user_id, name, description, price_per_night) VALUES (1, 'Beach House 1', 'A beautiful beach side property with a pool', 101);
INSERT INTO spaces (user_id, name, description, price_per_night) VALUES (1, 'Beach House 2', 'A beautiful beach side property with a pool', 102);
INSERT INTO spaces (user_id, name, description, price_per_night) VALUES (2, 'Glamping Pod 1', 'A glamping pod with all cooking facilities', 103);
INSERT INTO spaces (user_id, name, description, price_per_night) VALUES (2, 'Glamping Pod 2', 'A glamping pod with all cooking facilities', 104);
INSERT INTO spaces (user_id, name, description, price_per_night) VALUES (3, 'Country escape 1', 'A luxury cottage in the middle of the countryside', 105);
INSERT INTO spaces (user_id, name, description, price_per_night) VALUES (3, 'Country escape 2', 'A luxury cottage in the middle of the countryside', 106);

INSERT INTO availability (space_id, date, status) VALUES (1,'2025-01-01',TRUE);
INSERT INTO availability (space_id, date, status) VALUES (1,'2025-01-02',TRUE);
INSERT INTO availability (space_id, date, status) VALUES (1,'2025-02-03',TRUE);
INSERT INTO availability (space_id, date, status) VALUES (2,'2025-01-02',FALSE);
INSERT INTO availability (space_id, date, status) VALUES (3,'2025-01-02',FALSE);
INSERT INTO availability (space_id, date, status) VALUES (4,'2025-01-02',FALSE);
INSERT INTO availability (space_id, date, status) VALUES (5,'2025-01-02',TRUE);
INSERT INTO availability (space_id, date, status) VALUES (6,'2025-01-02',TRUE);

INSERT INTO bookings (night_id, user_id, status) VALUES (1, 2, 'pending');
INSERT INTO bookings (night_id, user_id, status) VALUES (1, 3, 'pending');
INSERT INTO bookings (night_id, user_id, status) VALUES (4, 2, 'confirmed');
INSERT INTO bookings (night_id, user_id, status) VALUES (4, 3, 'declined');
INSERT INTO bookings (night_id, user_id, status) VALUES (5, 1, 'confirmed');
INSERT INTO bookings (night_id, user_id, status) VALUES (6, 2, 'confirmed');
INSERT INTO bookings (night_id, user_id, status) VALUES (7, 1, 'pending');