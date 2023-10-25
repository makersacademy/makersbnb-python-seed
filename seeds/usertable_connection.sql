DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id TEXT PRIMARY KEY, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL, 
    passwordhash TEXT NOT NULL,
    phonenumber VARCHAR(20)
);

INSERT INTO users (id, username, email, passwordhash, phonenumber) VALUES ('4r8e9ujfoiuriej', 'benhurst', 'benhurst@email.com', 'password', '0123456789');
INSERT INTO users (id, username, email, passwordhash, phonenumber) VALUES ('rut9ehif', 'ovie1234', 'ovie@icloud.com', '12345678', '07764793090');
INSERT INTO users (id, username, email, passwordhash, phonenumber) values ('54y7r8euhi', 'marten', 'marten@google.com', '439rejofjsp0tijro5tsoir', '01234567890');