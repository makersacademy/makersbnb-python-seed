DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;




CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    password text
);

-- Then the table with the foreign key second.
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price float,
-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE TABLE dates (
    id SERIAL PRIMARY KEY,
    date date,
    confirmed boolean,
-- The foreign key name is always {other_table_singular}_id
    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date_id int,
    constraint fk_date foreign key(date_id)
        references dates(id)
        on delete cascade,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);