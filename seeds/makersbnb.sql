-- Delete existing tables.
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

DROP TABLE IF EXISTS dates;
DROP SEQUENCE IF EXISTS dates_id_seq;

DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Recreate tables.
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(6,2),
    host_id INT,
    constraint fk_host foreign key(host_id)
      references users(id)
      on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS dates_id_seq;
CREATE TABLE dates (
    id SERIAL PRIMARY KEY,
    date DATE,
    space_id INT,
    constraint fk_space foreign key(space_id)
      references spaces(id)
      on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date DATE,
    space_id INT,
    guest_id INT,
    confirmed BIT,
    constraint fk_guest foreign key(guest_id)
      references users(id)
      on delete cascade,
    constraint fk_space foreign key(space_id)
      references spaces(id)
      on delete cascade
);

-- Insert test records.
-- Users
INSERT INTO users (username, email, password) VALUES ('TestUser1', 'testuser1@testmail.co.uk', '1834f4b990e5d99eaf36be94a450314ad41fd4d18e9c788371dca8dc4c327a45');
INSERT INTO users (username, email, password) VALUES ('TestUser2', '2ndTestUser@ma1lt3st.com', '2ec6a6109f7b1ebb843a17b9dd037e012d161ef53b145006294b2483668b24ac');
INSERT INTO users (username, email, password) VALUES ('TestUser3', 'test.3.user@anuvatest.net', 'cfdcf9e9347c306b8664d40c17d93555b9f90412c0c985d53c8f1f81ac6c2b7e');

-- Spaces
INSERT INTO spaces (name, description, price, host_id) VALUES ('1 Test Drive', 'A small one bedroom flat with wet room and kitchenette.', 50.00, 1);
INSERT INTO spaces (name, description, price, host_id) VALUES ('2 Notteven Close', '3 bed, 3 bath, 3 beyond?', 115.99, 1);
INSERT INTO spaces (name, description, price, host_id) VALUES ('3 Letsby Avenue', 'Two bedroom terraced house close to the city centre.', 85.50, 2);
INSERT INTO spaces (name, description, price, host_id) VALUES ('4 Back End', 'Cosy detached cottage in the middle of nowhere.', 165.00, 2);
INSERT INTO spaces (name, description, price, host_id) VALUES ('5 Pastry Crescent', 'Converted boulangerie with space for a family of 4.', 99.99, 3);

-- Dates
INSERT INTO dates (date, space_id) VALUES ('2024-02-01', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-02-02', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-02-03', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-02-04', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-03-09', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-03-10', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-03-11', 1);
INSERT INTO dates (date, space_id) VALUES ('2024-03-12', 1);

INSERT INTO dates (date, space_id) VALUES ('2024-02-01', 2);
INSERT INTO dates (date, space_id) VALUES ('2024-02-02', 2);
INSERT INTO dates (date, space_id) VALUES ('2024-02-03', 2);
INSERT INTO dates (date, space_id) VALUES ('2024-02-04', 2);
INSERT INTO dates (date, space_id) VALUES ('2024-02-05', 2);
INSERT INTO dates (date, space_id) VALUES ('2024-02-06', 2);
INSERT INTO dates (date, space_id) VALUES ('2024-02-07', 2);

INSERT INTO dates (date, space_id) VALUES ('2024-11-21', 3);
INSERT INTO dates (date, space_id) VALUES ('2024-11-22', 3);
INSERT INTO dates (date, space_id) VALUES ('2024-12-09', 3);
INSERT INTO dates (date, space_id) VALUES ('2024-12-10', 3);
INSERT INTO dates (date, space_id) VALUES ('2024-12-11', 3);

INSERT INTO dates (date, space_id) VALUES ('2024-02-01', 4);
INSERT INTO dates (date, space_id) VALUES ('2024-04-01', 4);
INSERT INTO dates (date, space_id) VALUES ('2024-06-01', 4);

INSERT INTO dates (date, space_id) VALUES ('2024-01-15', 5);

-- Bookings
INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES ('2024-02-01', 1, 2, NULL);
INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES ('2024-02-01', 2, 2, NULL);
INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES ('2024-11-21', 3, 3, '1');
INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES ('2024-11-22', 3, 3, '1');
INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES ('2024-02-01', 1, 2, NULL);
INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES ('2024-11-22', 3, 1, '0');