DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    space_description text,
    space_price int
    -- date_id date
);

INSERT INTO spaces (space_name, space_description, space_price) VALUES ('Bagend', 'Hobbit Hole', 50);
INSERT INTO spaces (space_name, space_description, space_price) VALUES ('Isengard', 'Wizards Tower', 150);
INSERT INTO spaces (space_name, space_description, space_price) VALUES ('Minas Tirith', 'Big White City', 200);