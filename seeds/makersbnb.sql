-- add tables
-- users, spaces


DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    spaces TEXT
);


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

INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (1, 1, '01/01/2023', 'approved');
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (2, 2, '01/02/2023', 'approved');
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (3, 3, '01/03/2023', 'requested');
INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (4, 4, '01/04/2023', 'denied');