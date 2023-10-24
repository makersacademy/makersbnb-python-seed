-- add tables
-- users, spaces


DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    spaces TEXT
);


CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name TEXT,
    description TEXT,
    price_per_night INT,
    user_id INT
);


INSERT INTO users (username, spaces) VALUES ('user_1', 'space_1');
INSERT INTO users (username, spaces) VALUES ('user_2', 'space_2');

INSERT INTO 
    spaces (space_name, description, price_per_night, user_id)
    VALUES ('space_1', 'A nice space', 10, 1);
INSERT INTO 
    spaces (space_name, description, price_per_night, user_id)
    VALUES ('space_2', 'Another nice space', 20, 2);

-- AvailableDate

DROP TABLE IF EXISTS AvailableDates
DROP SEQUENCE IF EXISTS AvailableDates_id_seq;

CREATE TABLE AvailableDates (
    id SERIAL PRIMARY KEY,
    date_name TEXT,
    space_id FOREIGN KEY REFERENCES spaces(id)
);