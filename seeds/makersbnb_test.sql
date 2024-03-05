DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE TABLE spaces (id SERIAL PRIMARY KEY, description VARCHAR(255), price FLOAT, user_id INT, name VARCHAR(255));
CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (description, price, user_id, name) VALUES ('house with a pool', 99.99, 1,'pool house');
INSERT INTO spaces (description, price, user_id, name) VALUES ('house with a garden', 199.99, 2,'garden house');
INSERT INTO users (username, password) VALUES ('user1@test.com', 'password123');
INSERT INTO users (username, password) VALUES ('user2@test.com', 'password000');