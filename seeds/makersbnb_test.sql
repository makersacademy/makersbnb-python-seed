DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;

-- Then, we recreate them
CREATE TABLE spaces (id SERIAL PRIMARY KEY, description VARCHAR(255), price FLOAT, user_id INT, name VARCHAR(255), free_dates TEXT);
CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));
CREATE TABLE requests (id SERIAL PRIMARY KEY,  spaceid INT, date DATE, guestid INT);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (description, price, user_id, name, free_dates) VALUES ('house with a pool', 99.99, 1,'pool house', '["01-01-2024", "01-02-2024", "01-03-2024", "01-04-2024", "01-05-2024", 
"01-06-2024", "01-07-2024", "01-08-2024", "01-09-2024", "01-10-2024", 
"01-11-2024", "01-12-2024", "01-13-2024", "01-14-2024", "01-15-2024", 
"01-16-2024", "01-17-2024", "01-18-2024", "01-19-2024", "01-20-2024", 
"01-21-2024", "01-22-2024", "01-23-2024", "01-24-2024", "01-25-2024", 
"01-26-2024", "01-27-2024", "01-28-2024", "01-29-2024", "01-30-2024", 
"01-31-2024"]');
INSERT INTO users (username, password) VALUES ('user1@test.com', 'password123');
INSERT INTO users (username, password) VALUES ('user2@test.com', 'password000');
INSERT INTO requests (spaceid, date, guestid) VALUES (1, '2024-01-01', 1);