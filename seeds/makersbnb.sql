DROP TABLE IF EXISTS spaces;

-- Then, we recreate them
CREATE TABLE spaces (id SERIAL PRIMARY KEY, description VARCHAR(255), price FLOAT, user_id INT, name VARCHAR(255), fromdate DATE, todate DATE);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (description, price, user_id, name, fromdate, todate) VALUES ('house with a pool', 99.99, 1,'pool house', '2024-03-04', '2024-03-31');
INSERT INTO spaces (description, price, user_id, name, fromdate, todate) VALUES ('house with a garden', 199.99, 2,'garden house', '2024-04-01', '2024-04-30');