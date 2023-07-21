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
    availability text,
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
INSERT INTO users (username, user_password, email) VALUES ('Example User3', 'examplepassword2', 'exampleemail3@email.com');
INSERT INTO users (username, user_password, email) VALUES ('Example User4', 'examplepassword2', 'exampleemail4@email.com');


INSERT INTO spaces (name, description, price, availability, user_id) VALUES ('Example bnb', 'Examply cosy bnb', 100, '18-07-23, 19-07-23, 20-07-23', 2);
INSERT INTO spaces (name, description, price, availability, user_id) VALUES ('Example bnb2', 'Another cosy bnb', 200, '21-07-23, 22-07-23, 23-07-23', 1);
INSERT INTO spaces (name, description, price, availability, user_id) VALUES ('Example bnb3', 'Yet another cosy bnb', 500, '25-07-23, 26-07-23', 3);
INSERT INTO spaces (name, description, price, availability, user_id) VALUES ('Example bnb4', 'Yet another even cosier bnb', 500, '21-07-23, 22-07-23, 23-07-23', 1);
INSERT INTO spaces (name, description, price, availability, user_id) VALUES ('Example bnb5', 'Not so cosy bnb', 400, '24-07-23', 4);

INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 1, '01-04-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (2, 4, '01-05-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (2, 1, '01-06-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 2, '01-07-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 3, '01-08-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 4, '01-09-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (4, 1, '01-10-2023', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (4, 2, '01-01-2024', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 3, '01-12-2025', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (3, 4, '01-02-2026', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (2, 3, '03-08-2027', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 3, '01-08-2028', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 3, '05-08-2031', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (4, 3, '02-08-2030', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 2, '01-04-2025', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (3, 1, '01-02-2029', 'TBC');
INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (1, 2, '01-04-2023', 'TBC');
