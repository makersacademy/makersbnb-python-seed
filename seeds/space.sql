-- Deleting the table to avoid duplication:
DROP TABLE IF EXISTS space;

-- Creating a space table:
CREATE TABLE space (id SERIAL PRIMARY KEY, space_name TEXT, description TEXT, price_per_night INT, user_id INT, start_date TEXT, end_date TEXT);

-- Adding example space records
INSERT INTO space (space_name, description, price_per_night, user_id, start_date, end_date) VALUES ('test name1', 'test description1', 30 , 1, '2023/1/1', '2023/2/1');
INSERT INTO space (space_name, description, price_per_night, user_id, start_date, end_date) VALUES ('test name2', 'test description2', 30 , 1, '2023/1/1', '2023/2/1');
INSERT INTO space (space_name, description, price_per_night, user_id, start_date, end_date) VALUES ('test name3', 'test description3', 30 , 2, '2023/1/1', '2023/2/1');
INSERT INTO space (space_name, description, price_per_night, user_id, start_date, end_date) VALUES ('test name4', 'test description4', 30 , 3, '2023/1/1', '2023/2/1');