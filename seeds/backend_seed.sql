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
INSERT INTO users (email, password) VALUES ('Pixies', 'Rock');
INSERT INTO users (email, password) VALUES ('ABBA', 'Pop');
INSERT INTO users (email, password) VALUES ('Taylor Swift', 'Pop');
INSERT INTO users (email, password) VALUES ('Nina Simone', 'Jazz');

INSERT INTO properties (property_type, description, price, location, start_date, end_date, available, user_id) 
    VALUES ('Doolittle', 1989, 1);
INSERT INTO properties (property_type, description, price, location, start_date, end_date, available, user_id) 
    VALUES ('Surfer Rosa', 1988, 1);
INSERT INTO properties (property_type, description, price, location, start_date, end_date, available, user_id) 
    VALUES ('Waterloo', 1974, 2);
