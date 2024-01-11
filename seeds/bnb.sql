DROP TABLE if EXISTS bookings;
DROP TABLE if EXISTS spaces;
DROP TABLE if EXISTS users;

--SET lc_monetary = 'en_GB';  -- This doesn't work. Need to find out how to set money to £

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text,
    bookings int[]
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    location text,
    description text,
    price int,
    user_id int, 
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade,
    start_date date,
    end_date date
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date text,
    confirmed boolean,
    rejected boolean,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade,
    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade 
);

INSERT INTO users (username, email, password) VALUES ('test_username', 'test@test.com', 'password123');
INSERT INTO users (username, email, password) VALUES ('test_username2', 'test2@test.com', 'password123');

INSERT INTO spaces (space_name, location, description, price, user_id, start_date, end_date) VALUES ('3 bedroom apartment', 'London', 'city', 200, 1, '2024-02-01', '2025-02-01');
INSERT INTO spaces (space_name, location, description, price, user_id, start_date, end_date) VALUES ('Penthouse', 'Manchester', 'city', 150, 1, '2024-03-01', '2025-01-01');
INSERT INTO spaces (space_name, location, description, price, user_id, start_date, end_date) VALUES ('BnB villa', 'Rome', 'city', 300, 1, '2024-02-01', '2024-09-01');
INSERT INTO spaces (space_name, location, description, price, user_id, start_date, end_date) VALUES ('Town cottage', 'Newastle', 'city', 125, 1, '2024-03-01', '2024-11-01');

INSERT INTO bookings (date, confirmed, rejected, user_id, space_id) VALUES ('2024-01-01', False, False, 1, 1);
INSERT INTO bookings (date, confirmed, rejected, user_id, space_id) VALUES ('2024-01-02', False, False, 1, 2);
INSERT INTO bookings (date, confirmed, rejected, user_id, space_id) VALUES ('2024-01-03', False, False, 2, 2);