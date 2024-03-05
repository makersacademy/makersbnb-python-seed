DROP TABLE IF EXISTS spaces;

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    description VARCHAR(255),
    price INT,
    owner VARCHAR(255)
);


INSERT INTO spaces(name, location, description, price, owner) VALUES ('Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob');
INSERT INTO spaces(name, location, description, price, owner) VALUES ('Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim');
INSERT INTO spaces(name, location, description, price, owner) VALUES ('Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane');
INSERT INTO spaces(name, location, description, price, owner) VALUES ('Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan');
INSERT INTO spaces(name, location, description, price, owner) VALUES ('Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil');