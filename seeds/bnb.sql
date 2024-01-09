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
    date date,
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
INSERT INTO spaces (space_name, description, price, user_id, start_date, end_date) VALUES ('London', 'city', 200, 1, '2024-02-01', '2025-02-01');
INSERT INTO bookings (date, user_id, space_id) VALUES ('2024-01-01' ,1, 1);

