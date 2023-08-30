-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS properties;
DROP SEQUENCE IF EXISTS properties_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE SEQUENCE IF NOT EXISTS properties_id_seq;
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    property_type VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    available BOOLEAN NOT NULL,
-- The foreign key name is always {other_table_singular}_id
    user_id INTEGER,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email, password) VALUES ('test1@test.com', 'password123');
INSERT INTO users (email, password) VALUES ('test2@test.com', 'password1234');
INSERT INTO users (email, password) VALUES ('test3@test.com', 'password12345');
INSERT INTO users (email, password) VALUES ('test4@test.com', 'password123456');

INSERT INTO properties (property_type, description, price, location, start_date, end_date, available, user_id) 
    VALUES ('Flat', 'Sunny 2bdr flat in city centre', 100, Hackney, 2023-08-30, 2023-12-31, 1, 1 );
INSERT INTO properties (property_type, description, price, location, start_date, end_date, available, user_id) 
    VALUES ('Maisonette','Large 3bdr 2ba with spacious garden', 300, Brixton, 2023-08-30, 2023-12-31, 1, 2 );
INSERT INTO properties (property_type, description, price, location, start_date, end_date, available, user_id) 
    VALUES ('Annex','Double bed 2floor with ensuite', 80, Brighton, 2023-08-30, 2023-12-31, 1, 3 );
