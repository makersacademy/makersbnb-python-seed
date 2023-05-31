
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;

DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE TABLE users (
id SERIAL PRIMARY KEY,
email text,
password text
);

CREATE TABLE spaces (
id SERIAL PRIMARY KEY,
name text,
description text,
price float,
available_from date,
available_to date, 
user_id int, 
constraint fk_users foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE TABLE bookings (
id SERIAL PRIMARY KEY,
date_reserved date,
space_id int, 
constraint fk_spaces foreign key(space_id)
        references spaces(id)
        on delete cascade
);

INSERT INTO users (email, password) VALUES ('mrtester@gmail.com', 'GudPass91!');
INSERT INTO users (email, password) VALUES ('vlad@hotmail.com', 'Coolguy4');

INSERT INTO spaces (name, description, price, available_from, available_to, user_id) VALUES ('The Shack', 'A quaint little shed...', 20.00, '2023-01-01', '2023-12-25', 1);
INSERT INTO spaces (name, description, price, available_from, available_to, user_id) VALUES ('24 Farm Street', 'The country aroma is strong...', 40.00, '2023-01-01', '2023-12-25', 1);
INSERT INTO spaces (name, description, price, available_from, available_to, user_id) VALUES ('Castle Dracula', 'Dont let the dust put you off...', 500.00, '2023-01-01', '2023-12-25', 2);
INSERT INTO spaces (name, description, price, available_from, available_to, user_id) VALUES ('London Bachelor Pad', 'You cant afford this place..', 3000.00, '2023-01-01', '2023-12-25', 2);

INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-09-01', 1);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-09-02', 1);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-09-03', 1);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-09-04', 1);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-11-15', 2);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-11-16', 2);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-11-17', 2);
INSERT INTO bookings(date_reserved, space_id) VALUES ('2023-11-18', 2);
