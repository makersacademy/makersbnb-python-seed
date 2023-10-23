DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS dates;
DROP SEQUENCE IF EXISTS dates_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text,
    username text,
    password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    size int,
    location text,
    price float,
    user_id int,
    constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS dates_id_seq;
CREATE TABLE dates (
    id SERIAL PRIMARY KEY,
    date date,
    is_available boolean,
    space_id int,
    constraint fk_spaces foreign key(space_id)
    references spaces(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    is_confirmed boolean,
    space_id int,
    date_id int,
    booker_id int,
    owner_id int,
    constraint fk_spaces_bookings foreign key(space_id)
    references spaces(id)
    on delete cascade,
    constraint fk_dates foreign key(date_id)
    references dates(id)
    on delete cascade,
    constraint fk_bookers foreign key(booker_id)
    references users(id)
    on delete cascade,
    constraint fk_owners foreign key(owner_id)
    references users(id)
    on delete cascade
);