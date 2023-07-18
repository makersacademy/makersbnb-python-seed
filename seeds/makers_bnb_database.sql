DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS properties;
DROP SEQUENCE IF EXISTS properties_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  password text
);




CREATE TABLE properties (
  id SERIAL PRIMARY KEY,
  name text,
  description VARCHAR(355),
  price numeric,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  start_date date,
  end_date date,
  property_id int,
  constraint fk_property foreign key(property_id)
    references properties(id)
    on delete cascade,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email, password) VALUES ('asha@example.com', 'password1');
INSERT INTO users (email, password) VALUES ('lydia@example.com', 'password2');
INSERT INTO users (email, password) VALUES ('fahim@example.com', 'password3');
INSERT INTO users (email, password) VALUES ('gemma@example.com', 'password4');

INSERT INTO properties (name, description, price, user_id) VALUES ('Hackers Hideaway', 'A mystery place full of bugs', 50.00, 1);
INSERT INTO properties (name, description, price, user_id) VALUES ('Ma house', 'Its a very nice', 25.5, 1);
INSERT INTO properties (name, description, price, user_id) VALUES ('Makers HQ', 'Cosy and helpful', 100.00, 4);

INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-01-01', '2024-01-08', 1, 4);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-02-14', '2024-02-15', 2, 2);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-06-07', '2024-08-07', 3, 1);
INSERT INTO bookings (start_date, end_date, property_id, user_id) VALUES ('2024-01-10', '2024-01-16', 1, 3);
