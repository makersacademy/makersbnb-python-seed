DROP TABLE IF EXISTS users CASCADE;

-- Then, we recreate them
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255));

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email, password) VALUES ('user1', 'user1@example.com', 'abc123');
INSERT INTO users (name, email, password) VALUES ('user2', 'user2@yahoo.com', 'password123');
INSERT INTO users (name, email, password) VALUES ('user3', 'user3@gmail.com', 'letmein!');
