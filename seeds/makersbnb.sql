
-- First, we must delete (drop) all our tables and their dependent objects
DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS availabilities;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS users;

-- DROP TABLE IF EXISTS spaces CASCADE;
-- DROP TABLE IF EXISTS availabilities CASCADE;
-- DROP TABLE IF EXISTS bookings CASCADE;
-- DROP TABLE IF EXISTS users CASCADE;

-- DROP SEQUENCE IF EXISTS peeps_id_seq;  
-- DROP SEQUENCE IF EXISTS users_id_seq;  

-- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;  
-- CREATE SEQUENCE IF NOT EXISTS users_id_seq;  


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(10, 2),
    owner_id INTEGER REFERENCES users(id)
);

-- CREATE TABLE availabilities (
--     id SERIAL PRIMARY KEY,
--     space_id INTEGER REFERENCES spaces(id),
--     available_date DATE
-- );

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    space_id INTEGER REFERENCES spaces(id),
    checkin_date DATE,
    -- checkout_date DATE,
    is_approved BOOLEAN DEFAULT FALSE
);

-- Finally, we add any records that are needed for the tests to run
-- Insert sample users here.

INSERT INTO users (username, email, password) VALUES ('liza_77', 'liza@liza.com', 'password123');

-- Insert sample peeps (messages) here.

INSERT INTO spaces (name, description, price, owner_id) VALUES ('The Devonshire Laisure & Spa', 'This is a calm, quiet place where you can completely relax and gain strength', 180, 1);
INSERT INTO spaces (name, description, price, owner_id) VALUES ('Helmsley Black Swan Appartments', 'this apartment is located in the city centre', 250, 1);


-- INSERT INTO availabilities (space_id, available_date) VALUES (2, '2023-12-21');

INSERT INTO bookings (user_id, space_id, checkin_date, is_approved) VALUES (1, 2, '2023-12-21', True);









