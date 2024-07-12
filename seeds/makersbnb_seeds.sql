-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;

DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
    username text
);
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price_per_night FLOAT(10),
    available_from DATE, 
    available_to DATE,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    listing_id INT NOT NULL,
    booked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    booker_id INT NOT NULL,
    check_in DATE,
    check_out DATE,
    CONSTRAINT fk_listing
        FOREIGN KEY(listing_id) 
        REFERENCES listings(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_booker
        FOREIGN KEY(booker_id) 
        REFERENCES users(id)
        ON DELETE CASCADE
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username) VALUES ('marya_test');

INSERT INTO listings (name, description, price_per_night, available_from, available_to, user_id) VALUES ('test-cottage', 'nice cottage by the beach', 25.00, '2024-01-01', '2024-10-01', 1);

INSERT INTO bookings (listing_id, booker_id, check_in, check_out) VALUES (1, 1, '2024-01-01', '2024-01-02');
