DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int
    -- date_id date
);

INSERT INTO spaces (name, description, price) VALUES ('Bagend', 'Hobbit Hole', 50);
INSERT INTO spaces (name, description, price) VALUES ('Isengard', 'Wizards Tower', 150);
INSERT INTO spaces (name, description, price) VALUES ('Minas Tirith', 'Big White City', 200);