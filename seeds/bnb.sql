DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int,
    start_date text,
    end_date text
);

INSERT INTO spaces (name, description, price, start_date, end_date) VALUES ('Bagend', 'Hobbit Hole', 50, '25-12-23', '30-12-23');
INSERT INTO spaces (name, description, price, start_date, end_date) VALUES ('Isengard', 'Wizards Tower', 150, '25-12-23', '30-12-23');
INSERT INTO spaces (name, description, price, start_date, end_date) VALUES ('Minas Tirith', 'Big White City', 200, '25-12-23', '30-12-23');