DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS availabilities;

CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  price float,
  description text,
  user_id int,
  constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  booking_start_date DATE,
  booking_end_date DATE,
  space_id INT,
  constraint fk_space foreign key(space_id) references spaces(id) ON DELETE CASCADE
);

INSERT INTO spaces (name, price, description, user_id) VALUES ('London Bridge', 15.99, 'It isnt the one you think it is', 1);
INSERT INTO spaces (name, price, description, user_id) VALUES ('Big Ben', 97.43, 'Tall clock, its loud', 3);
INSERT INTO spaces (name, price, description, user_id) VALUES ('Gherkin', 46.90, 'Americans call it the pickle', 2);
INSERT INTO spaces (name, price, description, user_id) VALUES ('The Shard', 546.00, 'The sky garden is free', 2);

INSERT INTO bookings (booking_start_date, booking_end_date, space_id) VALUES ('2024-10-23', '2024-10-23', 1);
INSERT INTO bookings (booking_start_date, booking_end_date, space_id) VALUES ('2024-05-21', '2024-05-21', 3);
INSERT INTO bookings (booking_start_date, booking_end_date, space_id) VALUES ('2024-12-02', '2024-12-02', 4);
INSERT INTO bookings (booking_start_date, booking_end_date, space_id) VALUES ('2024-06-16', '2024-06-16', 2);


CREATE TABLE availabilities (
  id SERIAL PRIMARY KEY,
  availability_from DATE,
  availability_to DATE,
  space_id INT,
  constraint fk_space foreign key(space_id) references spaces(id) ON DELETE CASCADE
);


INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-10-12', '2024-10-25', 1);
INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-05-21', '2024-06-01', 3);
INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-11-02', '2024-12-02', 4);
INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-06-10', '2024-06-28', 2);