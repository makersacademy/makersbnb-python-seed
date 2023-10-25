Users (user id,name,username,password,email,phone_number)
Spaces (user id, space id, name, description, price-per-night)
Availablity (space id, date-not-available)

CREATE TABLE Users (
  user id SERIAL PRIMARY KEY,
  username text,
  name text,
  password varchar(255),
  email,
  phone number
);



-- Then the table with the foreign key second.
CREATE TABLE Spaces (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
-- The foreign key name is always {other_table_singular}_id
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade