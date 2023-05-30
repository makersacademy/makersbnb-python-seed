-- Drop tables if they already exist
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS listings CASCADE;

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

INSERT INTO users (username, password, email)
VALUES 
('User1', 'Password1', 'user1@email.com'),
('User2', 'Password2', 'user2@email.com'),
('User3', 'Password3', 'user3@email.com');

-- Insert into listings table
INSERT INTO listings (name, description, price, user_id)
VALUES 
('Charming Cottage', 'A small, cozy cottage in the woods.', 100.00, 1),
('City Apartment', 'An apartment in the heart of the city.', 150.00, 2),
('Beach House', 'A house with a beautiful ocean view.', 200.00, 3);