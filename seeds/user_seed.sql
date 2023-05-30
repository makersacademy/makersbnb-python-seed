DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    password TEXT
);

INSERT INTO users (name, username, email, password) VALUES ('Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123');