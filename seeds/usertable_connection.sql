DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id serial PRIMARY KEY, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL, 
    passwordhash TEXT NOT NULL,
    phonenumber VARCHAR(20)
);

INSERT INTO users (username, email, passwordhash, phonenumber) VALUES ('benhurst', 'benhurst@email.com', 'password', '0123456789');
INSERT INTO users (username, email, passwordhash, phonenumber) VALUES ('ovie1234', 'ovie@icloud.com', '12345678', '07764793090');
INSERT INTO users (username, email, passwordhash, phonenumber) values ('marten', 'marten@google.com', '439rejofjsp0tijro5tsoir', '01234567890');