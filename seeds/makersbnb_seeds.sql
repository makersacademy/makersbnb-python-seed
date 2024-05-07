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

INSERT INTO users (username, password) VALUES ('Andrew', 'Password1!');
INSERT INTO users (username, password) VALUES ('Benedict', 'Password2!');
INSERT INTO users (username, password) VALUES ('Melissa', 'Password3!');
INSERT INTO users (username, password) VALUES ('Umut', 'Password4!');
INSERT INTO users (username, password) VALUES ('Tomi', 'Password5!');
INSERT INTO users (username, password) VALUES ('Jawad', 'Password6!');

INSERT INTO spaces (name, description, price, user_id) VALUES ('Test Name 1', 'Test Description 1', 10, 1);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Test Name 2', 'Test Description 2', 50, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Test Name 3', 'Test Description 3', 30, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Test Name 4', 'Test Description 4', 10, 1);

INSERT INTO dates (date, confirmed, space_id) VALUES ('20-01-2024', True, 1);
INSERT INTO dates (date, confirmed, space_id) VALUES ('21-01-2024', False, 2);
INSERT INTO dates (date, confirmed, space_id) VALUES ('22-01-2024', False, 2);
INSERT INTO dates (date, confirmed, space_id) VALUES ('23-01-2024', True, 3);
INSERT INTO dates (date, confirmed, space_id) VALUES ('24-01-2024', False, 1);
INSERT INTO dates (date, confirmed, space_id) VALUES ('25-01-2024', False, 4);

INSERT INTO bookings (date_id, user_id) VALUES (1, 4);
INSERT INTO bookings (date_id, user_id) VALUES (4, 3);
INSERT INTO bookings (date_id, user_id) VALUES (5, 2);
INSERT INTO bookings (date_id, user_id) VALUES (5, 5);

