DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS users_spaces;
DROP SEQUENCE IF EXISTS users_spaces_id_seq;
DROP TABLE IF EXISTS spaces_bookings;
DROP SEQUENCE IF EXISTS spaces_bookings_id_seq;
DROP TABLE IF EXISTS users_bookings;
DROP SEQUENCE IF EXISTS users_bookings_id_seq;

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
    booking_id int,
    owner int
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date date,
    space_id int,
    user_id int
);

CREATE TABLE users_spaces (
    user_id int,
    space_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_space foreign key(space_id) references spaces(id) on delete cascade,
    PRIMARY KEY (user_id, space_id)
);

CREATE TABLE spaces_bookings (
    space_id int,
    booking_id int,
    constraint fk_space foreign key(space_id) references spaces(id) on delete cascade,
    constraint fk_booking foreign key(booking_id) references bookings(id) on delete cascade,
    PRIMARY KEY (space_id, booking_id)
);

CREATE TABLE users_bookings (
    user_id int,
    booking_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_booking foreign key(booking_id) references bookings(id) on delete cascade,
    PRIMARY KEY (user_id, booking_id)
);

INSERT INTO users 
    (name, email, password) 
VALUES 
    ('Oliver', 'oliver@test.com', 'password111!'),
    ('Kate', 'kate@test.com', 'password222!'),
    ('Joan', 'joan@test.com', 'password333$'),
    ('Saamiya', 'saamiya@test.com', 'password444$');

INSERT INTO spaces 
    (space_name, description, price, location, booking_id, owner) 
VALUES 
    ('London Flat', 'City vibes', 500.00, 'London', 1, 1),
    ('Manchester House', 'It is a house innit', 400.00, 'Manchester', 2, 2),
    ('Derby Farmhouse', 'Come and see the cows', 100.00, 'Derby', 3, 3),
    ('Cotswolds Manor', 'Posh vibes', 1000.00, 'Cotswolds', 4, 4);

INSERT INTO bookings
    (date, space_id, user_id) 
VALUES 
    ('2023-06-23', 1, 4),
    ('2023-07-04', 2, 3),
    ('2023-07-18', 3, 1),
    ('2023-06-15', 4, 2);