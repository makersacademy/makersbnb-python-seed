DROP TABLE IF EXISTS makersbnb;
DROP SEQUENCE IF EXISTS makersbnb_id_seq;


CREATE SEQUENCE IF NOT EXISTS makersbnb_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name VARCHAR(255),
    space_location VARCHAR(255),
    space_description VARCHAR(255),
    space_price INT,
    space_owner VARCHAR(255)
);


INSERT INTO spaces(space_name, space_location, space_description, space_price, space_owner) VALUES ('Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob');
INSERT INTO spaces(space_name, space_location, space_description, space_price, space_owner) VALUES ('Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim');
INSERT INTO spaces(space_name, space_location, space_description, space_price, space_owner) VALUES ('Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane');
INSERT INTO spaces(space_name, space_location, space_description, space_price, space_owner) VALUES ('Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan');
INSERT INTO spaces(space_name, space_location, space_description, space_price, space_owner) VALUES ('Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil');