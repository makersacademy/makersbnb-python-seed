DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    size INTEGER,
    price INTEGER,
    owner_id INTEGER
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id INTEGER,
    booker_id INTEGER,
    start_date date,
    end_date date,
    confirmed boolean
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (first_name, last_name, email, password) VALUES ('Leonardo', 'Leonardopoulos', 'leonar364@net.com','pug3&');
INSERT INTO users (first_name, last_name, email, password) VALUES ('Donatello', 'Donatellis', 'donat5784@post.com', 'don9876&');
INSERT INTO users (first_name, last_name, email, password) VALUES ('Michelangelo', 'Michelangelou', 'mich937@lst.gr','Poodlehd3&');
INSERT INTO users (first_name, last_name, email, password) VALUES ('Raphael', 'Raphaelidis', 'raph086@pet.com', 'shitsugewv9%');

INSERT INTO spaces (name, description, size, price, owner_id) VALUES ('Beach House', 'The most relaxing place', 187, 999, 3);
INSERT INTO spaces (name, description, size, price, owner_id) VALUES ('Lake House', 'The most quiet place', 157, 879, 3);
INSERT INTO spaces (name, description, size, price, owner_id) VALUES ('City Centre House', 'The most popular place', 55, 276, 3);



