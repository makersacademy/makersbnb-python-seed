DROP TABLE IF EXISTS makersbnb;
DROP SEQUENCE IF EXISTS makersbnb_id_seq;


CREATE SEQUENCE IF NOT EXISTS makersbnb_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name VARCHAR(255),
    space_description VARCHAR(255),
    space_price VARCHAR(255),
    space_owner VARCHAR(255)
);


INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Bob House', '3 bedrooms, 2 bathrooms, Victorian-era property', '£300 per night', 'Bob');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Jim House', '3 bedrooms, 3 bathrooms, Modern property', '£350 per night', 'Jim');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Jane House', '4 bedrooms, 2 bathrooms, Georgian-era property', '£450 per night', 'Jane');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Megan House', '5 bedrooms, 5 bathrooms, Contemporary property', '£600 per night', 'Megan');
INSERT INTO spaces(space_name, space_description, space_price, space_owner) VALUES ('Phil House', '2 bedrooms, 1 bathrooms, Barn-style property', '£200 per night', 'Phil');