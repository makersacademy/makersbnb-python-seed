DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS user_id_seq;
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listing_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email text, password text, user_name text);
CREATE SEQUENCE IF NOT EXISTS listing_id_sequence;
CREATE TABLE IF NOT EXISTS listings (id SERIAL PRIMARY KEY, name text, description text, cost int, user_id int);

INSERT INTO users (email, password, user_name) VALUES ('test-email-1', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42', 'Test User 1');
INSERT INTO users (email, password, user_name) VALUES ('test-email-2', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2', 'Test User 2');
INSERT INTO users (email, password, user_name) VALUES ('test-email-3', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600', 'Test User 3');

INSERT INTO listings (name, description, cost, user_id) VALUES ('first-test-listing', 'Description 1', 45, 1);
INSERT INTO listings (name, description, cost, user_id) VALUES ('second-test-listing', 'Description 2', 70, 1);
INSERT INTO listings (name, description, cost, user_id) VALUES ('third-test-listing', 'Description 3', 35, 2);
INSERT INTO listings (name, description, cost, user_id) VALUES ('fourth-test-listing', 'Description 4', 50, 3);
INSERT INTO listings (name, description, cost, user_id) VALUES ('fifth-test-listing', 'Description 5', 100, 2);
INSERT INTO listings (name, description, cost, user_id) VALUES ('sixth-test-listing', 'Description 6', 85, 1);
