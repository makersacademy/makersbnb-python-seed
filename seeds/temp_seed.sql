DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS bookings;

CREATE TABLE users(
    id SERIAL,
    email_address VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE spaces(
    id SERIAL,
    userid INT,
    title VARCHAR(255),
    start_date DATE,
    end_date DATE,
    price REAL
);

CREATE TABLE bookings(
    id SERIAL,
    user_id INT,
    space_id INT,
    booking_date DATE
);

INSERT INTO users (email_address, password) VALUES ('harrydon725','password123');
INSERT INTO users (email_address,password) VALUES ('Jsanyang21','1234');

INSERT INTO spaces (userid, title, start_date, end_date, price) VALUES (1, 'Beach house','2024-06-01','2024-09-01',50.0);
INSERT INTO spaces (userid, title, start_date, end_date, price) VALUES (2, 'Winter Lodge','2024-10-01','2025-01-01',60.0);

INSERT INTO bookings (user_id, space_id, booking_date) VALUES (1,2,'2024-05-06');
INSERT INTO bookings (user_id, space_id, booking_date) VALUES (2,1,'2024-05-07');



