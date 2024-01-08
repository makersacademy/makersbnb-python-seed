DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    passw VARCHAR(255)
);


INSERT INTO users (email, passw) VALUES ('user_1@mail.com', 'makersbnb2')
INSERT INTO users (email, passw) VALUES ('user_2@mail.com', 'qwerty123')
INSERT INTO users (email, passw) VALUES ('user_3@mail.com', 'makersbnb1')