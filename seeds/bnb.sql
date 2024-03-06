-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate the
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    email VARCHAR(255), 
    forename VARCHAR(255), 
    surname VARCHAR(255), 
    phone_number VARCHAR(255), 
    password VARCHAR(255));

CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255), 
    description VARCHAR(255), 
    price_per_night FLOAT, 
    date_range_from DATE, 
    date_range_to DATE,   
    host_id int,
        constraint fk_author foreign key(host_id)
        references users(id)
    on delete cascade);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings(
    id SERIAL PRIMARY KEY, 
    check_in DATE, 
    check_out DATE,
    booking_status VARCHAR(255),
    CONSTRAINT chk_booking_status CHECK (booking_status IN ('Pending', 'Confirmed', 'Rejected', 'Cancelled')),
    host_id int,
        foreign key(host_id)
        references users(id)
    on delete cascade,
    guest_id int,
        foreign key(guest_id)
        references users(id)
    on delete cascade,
    listings_id int,
        foreign key(listings_id)
        references listings(id)
    on delete cascade);

-- INSERTING VALUES TO users

INSERT INTO users (email, forename, surname, phone_number, password) VALUES ('luckyone@gmail.com', 'jack', 'Lucky', '02123456711', '@12Cupoftea');
INSERT INTO users (email, forename, surname, phone_number, password) VALUES ('example@example.com', 'John', 'Doe', '01234567890', 'P@ssw0rd123');
INSERT INTO users (email, forename, surname, phone_number, password) VALUES ('test@test.com', 'Alice', 'Smith', '09876543210', 'SecurePassword!');
INSERT INTO users (email, forename, surname, phone_number, password) VALUES ('user123@gmail.com', 'Emily', 'Johnson', '03123456789', 'SecretPass123');
INSERT INTO users (email, forename, surname, phone_number, password) VALUES ('johndoe@example.com', 'John', 'Doe', '07777777777', 'Password1234');
INSERT INTO users (email, forename, surname, phone_number, password) VALUES ('janedoe@example.com', 'Jane', 'Doe', '05555555555', 'DoeJane123');



-- INSERTING VALUES TO listings

INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Not So Haunted House', 'This house is definitely not haunted', 29.99, '2024-02-12', '2024-02-19', 1);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Sunny Hideaway', 'Escape to this sun-filled retreat surrounded by nature', 69.99, '2024-03-01', '2024-06-07', 2);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Seaside Cottage', 'Experience coastal living in this charming seaside cottage', 89.99, '2024-03-10', '2024-09-22', 3);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Mountain Chalet', 'Cozy up by the fireplace in this picturesque mountain chalet', 99.99, '2024-03-05', '2024-04-05', 3);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Urban Studio', 'Immerse yourself in city life with this stylish urban studio', 79.99, '2024-03-02', '2025-03-08', 2);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Lakefront Cabin', 'Enjoy peaceful lakeside living in this cozy cabin', 109.99, '2024-03-03', '2025-03-09', 1);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Tranquil Retreat', 'Find serenity in this secluded retreat nestled in the woods', 79.99, '2024-03-01', '2025-07-05', 3);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('City View Apartment', 'Enjoy stunning city views from this modern apartment', 129.99, '2024-03-10', '2026-04-10', 3);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Beachfront Bungalow', 'Wake up to the sound of waves in this beachfront bungalow', 149.99, '2024-03-05', '2025-02-12', 2);
INSERT INTO listings (name, description, price_per_night, date_range_from, date_range_to, host_id) VALUES ('Country Farmhouse', 'Experience country living in this charming farmhouse', 99.99, '2024-03-02', '2023-03-08', 4);

-- INSERTING VALUES INTO bookings

INSERT INTO bookings (check_in, check_out, booking_status, host_id, guest_id, listings_id) VALUES ('2024-03-10', '2024-09-22', 'Confirmed', 3, 4, 3);
INSERT INTO bookings (check_in, check_out, booking_status, host_id, guest_id, listings_id) VALUES ('2024-03-10', '2024-04-22', 'Pending', 2, 5, 5);
INSERT INTO bookings (check_in, check_out, booking_status, host_id, guest_id, listings_id) VALUES ('2024-03-10', '2024-03-17', 'Rejected', 3, 6, 7);
INSERT INTO bookings (check_in, check_out, booking_status, host_id, guest_id, listings_id) VALUES ('2024-03-10', '2024-06-22', 'Cancelled', 3, 2, 3);