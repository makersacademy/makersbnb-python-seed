DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    price INTEGER,
    size INTEGER,
    description VARCHAR(255)
);

INSERT INTO spaces (name, location, price, size, description) VALUES ('Cozy Corner', 'London', 120, 2, 'Warm and inviting space with a cozy atmosphere.');
INSERT INTO spaces (name, location, price, size, description) VALUES ('Serene Spot', 'Manchester', 95, 1, 'Tranquil setting for a peaceful and relaxing experience.');
INSERT INTO spaces (name, location, price, size, description) VALUES ('Tranquil Haven', 'Birmingham', 110, 3, 'A haven of tranquility with spacious and comfortable surroundings.');
INSERT INTO spaces (name, location, price, size, description) VALUES ('Peaceful Retreat', 'Edinburgh', 140, 2, 'Escape to a peaceful retreat with calming ambiance and serenity.');
