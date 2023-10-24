-- add tables
-- users, spaces

DROP TABLE IF EXISTS AvailableDates;
DROP SEQUENCE IF EXISTS AvailableDates_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq; 
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    spaces TEXT
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name TEXT,
    description TEXT,
    price_per_night INT,
    user_id INT
);



CREATE TABLE bookings (
    user_id SERIAL PRIMARY KEY,
    space_id INT,
    booking_date TEXT,
    booking_status TEXT
);





INSERT INTO users (username, spaces) VALUES ('user_1', 'space_1');
INSERT INTO users (username, spaces) VALUES ('user_2', 'space_2');

INSERT INTO 
    spaces (space_name, description, price_per_night, user_id)
    VALUES ('space_1', 'A nice space', 10, 1);
INSERT INTO 
    spaces (space_name, description, price_per_night, user_id)
    VALUES ('space_2', 'Another nice space', 20, 2);

-- AvailableDate


CREATE TABLE AvailableDates (
    id SERIAL PRIMARY KEY,
    date_name TEXT,
    space_id INT,
    CONSTRAINT fk_space_id
        FOREIGN KEY(space_id)
        REFERENCES spaces(id)
        ON DELETE CASCADE
        -- ^ If a space is deleted, the associated available date(s) will also be deleted, carry it over to bookings someway...
);

INSERT INTO AvailableDates (date_name, space_id)
    VALUES ('12/11/03', 1);
INSERT INTO AvailableDates (date_name, space_id)
    VALUES ('11/11/00', 2); 
-- Here i found out sql doesnt accept double "" quotes GRRR
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (1, 1, '01/01/2023', 'approved');
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (2, 2, '01/02/2023', 'approved');
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (3, 3, '01/03/2023', 'requested');
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (4, 4, '01/04/2023', 'denied');