DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS req_id_seq;
DROP SEQUENCE IF EXISTS space_id_seq;
DROP TABLE IF EXISTS Spaces;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    passw VARCHAR(255)
);

CREATE TABLE Spaces(
    id SERIAL PRIMARY KEY,
    title text,
    space_description text,
    price float,
    daterange text,
    user_id int
);

CREATE TABLE requests(
    req_id int,
    space_id int,
    date_req text,
    stat text,
    constraint fk_spaces foreign key(space_id)
    references spaces(id)
    on delete cascade,
    constraint fk_users foreign key(req_id)
    references users(id)
    on delete cascade
);
INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title','This is some test description',65.75,'2024-01-12-2024-01-31',1);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title2','This is some test description',25.00,'2024-01-14-2024-01-29',1);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title3','This is some test description',135.50,'2024-01-12-2024-02-05',2);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title4','This is some test description',19.95,'2024-01-21-2024-01-31',2);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title5','This is some test description',1037.63,'2024-01-12-2024-01-19',3);

INSERT INTO users (email, passw) VALUES ('user_1@mail.com', 'makersbnb2');
INSERT INTO users (email, passw) VALUES ('user_2@mail.com', 'qwerty123');
INSERT INTO users (email, passw) VALUES ('user_3@mail.com', 'makersbnb1');