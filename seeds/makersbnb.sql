-- Drop tables if they already exist
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS listings CASCADE;
DROP TABLE IF EXISTS availability CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    actualname text,
    password text,
    email text
);

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price DECIMAL(10, 2),
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);

CREATE TABLE availability (
    id SERIAL PRIMARY KEY,
    listing_id INT,
    available_date DATE,
    FOREIGN KEY(listing_id) REFERENCES listings(id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT,
    listing_id INT,
    booking_date DATE,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_listing FOREIGN KEY(listing_id) REFERENCES listings(id) ON DELETE CASCADE
);

INSERT INTO users (username, actualname, email, password)
VALUES 
('User1', 'Actual Name 1', 'user1@email.com', 'Password1'),
('User2', 'Actual Name 2', 'user2@email.com', 'Password2'),
('User3', 'Actual Name 3', 'user3@email.com', 'Password3');

-- Insert into listings table
INSERT INTO listings (name, description, price, user_id)
VALUES 
('Charming Cottage', 'A small, cozy cottage in the woods.', 100.00, 1),
('City Apartment', 'An apartment in the heart of the city.', 150.00, 2),
('Beach House', 'A house with a beautiful ocean view.', 200.00, 3);

INSERT INTO availability (listing_id, available_date)
VALUES 
(1, '2023-06-05'),
(1, '2023-06-06'),
(1, '2023-06-07'),
(2, '2023-06-08'),
(2, '2023-06-09'),
(2, '2023-06-10'),
(3, '2023-06-11'),
(3, '2023-06-12'),
(3, '2023-06-13');

INSERT INTO bookings (user_id, listing_id, booking_date)
VALUES 
(1, 1, '2023-06-15'),
(2, 2, '2023-06-18'),
(3, 3, '2023-06-23');

