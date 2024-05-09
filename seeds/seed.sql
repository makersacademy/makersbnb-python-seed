DROP TABLE IF EXISTS users_spaces_requests;
DROP SEQUENCE IF EXISTS users_spaces_requests_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
-- Create the second table.
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  owner int,
  name text,
  description text,
  price_per_night int,
  start_date date,
  end_date date,
  constraint fk_owner foreign key(owner) references users(id) on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS users_spaces_requests_id_seq;
-- Create the join table.
CREATE TABLE users_spaces_requests (
  user_id int,
  space_id int,
  start_date date,
  end_date date,
  constraint fk_user foreign key(user_id) references users(id) on delete cascade,
  constraint fk_space foreign key(space_id) references spaces(id) on delete cascade,
  PRIMARY KEY (user_id, space_id)
);

INSERT INTO users (email, password) VALUES ('test1@gmail.com', 'password123'); 
INSERT INTO users (email, password) VALUES ('test2@gmail.com', 'password123');
INSERT INTO users (email, password) VALUES ('test3@gmail.com', 'password123'); 

INSERT INTO spaces (owner, name, description, price_per_night, start_date, end_date) VALUES (1, 'venue #1', 'desc #1', 50, '2024-01-01', '2024-01-08');
INSERT INTO spaces (owner, name, description, price_per_night, start_date, end_date) VALUES (1, 'venue #2', 'desc #2', 60, '2024-04-04', '2024-05-05');
INSERT INTO spaces (owner, name, description, price_per_night, start_date, end_date) VALUES (1, 'venue #3', 'desc #3', 70, '2024-01-01', '2024-01-05');
INSERT INTO spaces (owner, name, description, price_per_night, start_date, end_date) VALUES (2, 'venue #4', 'desc #4', 80, '2024-01-03', '2024-02-03');
INSERT INTO spaces (owner, name, description, price_per_night, start_date, end_date) VALUES (2, 'venue #5', 'desc #5', 90, '2024-02-04', '2024-02-05');

INSERT INTO users_spaces_requests (user_id, space_id, start_date, end_date) VALUES (1, 2, '2024-01-01', '2024-01-08');
INSERT INTO users_spaces_requests (user_id, space_id, start_date, end_date) VALUES (2, 3, '2024-04-04', '2024-05-05');
INSERT INTO users_spaces_requests (user_id, space_id, start_date, end_date) VALUES (3, 4, '2024-01-01', '2024-01-05');
INSERT INTO users_spaces_requests (user_id, space_id, start_date, end_date) VALUES (2, 4, '2024-01-03', '2024-02-03');