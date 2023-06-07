DROP TABLE IF EXISTS requests;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;

DROP SEQUENCE IF EXISTS users_id_seq;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP SEQUENCE IF EXISTS requests_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name text,
    last_name text,
    email text,
    password text
);


CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    title text,
    description text,
    price money,
    date_range date,
    -- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    owner_id int,
    constraint fk_owner foreign key(owner_id)
    references users(id)
    on delete cascade,
    visitor_id int,
    constraint fk_visitor foreign key(visitor_id)
    references users(id)
    on delete cascade,
    space_id int,
    constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade,
    request_date date,
    confirmed boolean
);

insert into users (first_name, last_name, email, password) values ('testfirstname', 'testlastname', 'test@gmail.com', 'test123');

insert into spaces (title, description, price, date_range, user_id) values ('test_title', 'test_description', 50.00, '2023-01-08', 1),
('test_title2', 'test_description2', 60.00, '2023-05-10', 1);