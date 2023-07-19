DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    user_password text,
    email text
);


CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int,
    availablility text,
    user_id int
);


CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    user_id int,
    space_id int,
    date_to_book text,
    request_status text,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_space foreign key(space_id) references spaces(id) on delete cascade
    -- PRIMARY KEY (user_id, space_id)
);


INSERT INTO users (username, user_password, email) VALUES ('Example User', 'examplepassword', 'exampleemail@email.com');
INSERT INTO users (username, user_password, email) VALUES ('Example User2', 'examplepassword2', 'exampleemail2@email.com');

INSERT INTO spaces (name, description, price, availability, user_id) VALUES ('Example bnb', 'Examply cosy bnb', 100, '18/07/23, 19/07/23, 20/07/23', 2);

