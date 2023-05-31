DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    username VARCHAR(20) UNIQUE,
    password VARCHAR(64),
    email VARCHAR(64)
);

CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    price INTEGER,
    name VARCHAR(20),
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    listing_id INTEGER,
    total FLOAT,
    start_date DATE,
    end_date DATE,
    confirmed BOOLEAN,
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users (name, username, email, password) 
VALUES ('Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123');

INSERT INTO users (name, username, email, PASSWORD)
VALUES('Owner McOwner', 'owner', 'owner@email.com', 'password123');

INSERT INTO listings (user_id, price, name, description)
VALUES(1, 150, 'name', 'listing description');

INSERT INTO listings (user_id, price, name, description)
VALUES(1, 300, 'name', 'listing description');


