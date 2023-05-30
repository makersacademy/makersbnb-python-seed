DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    email text,
    password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    description text,
    price float,
    location text,
    user_id int
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date date,
    space_id int,
    user_id int
);

INSERT INTO users 
    (name, email, password) 
VALUES 
    ('Oliver', 'oliver@test.com', 'password111!'),
    ('Kate', 'kate@test.com', 'password222!'),
    ('Joan', 'joan@test.com', 'password333$'),
    ('Saamiya', 'saamiya@test.com', 'password444$');

INSERT INTO spaces 
    (space_name, description, price, location, user_id) 
VALUES 
    ('London Flat', 'City vibes', 500.00, 'London', 1),
    ('Manchester House', 'It is a house innit', 400.00, 'Manchester', 2),
    ('Derby Farmhouse', 'Come and see the cows', 100.00, 'Derby', 3),
    ('Cotswolds Manor', 'Posh vibes', 1000.00, 'Cotswolds', 4);

INSERT INTO bookings
    (date, space_id, user_id) 
VALUES 
    ('2023-06-23', 1, 4),
    ('2023-07-04', 2, 3),
    ('2023-07-18', 3, NULL),
    ('2023-06-15', 4, NULL);