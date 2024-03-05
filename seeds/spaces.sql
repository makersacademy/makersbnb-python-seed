DROP TABLE IF EXISTS spaces;

CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  price float,
  description text,
  user_id int,
  constraint fk_user foreign key(user_id) references users(id) on delete cascade
);


INSERT INTO spaces (name, price, description, user_id) VALUES ('London Bridge', 15.99, 'It isnt the one you think it is', 1);
INSERT INTO spaces (name, price, description, user_id) VALUES ('Big Ben', 97.43, 'Tall clock, its loud', 3);
INSERT INTO spaces (name, price, description, user_id) VALUES ('Gherkin', 46.90, 'Americans call it the pickle', 2);
INSERT INTO spaces (name, price, description, user_id) VALUES ('The Shard', 546.00, 'The sky garden is free', 2);
