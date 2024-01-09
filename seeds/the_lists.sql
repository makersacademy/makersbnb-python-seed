DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings(
    id SERIAL PRIMARY KEY, title varchar(255), description text, price int
);

INSERT INTO listings (title, description, price) VALUES ('First Listing', 'This is a description for the first listing', 1);
INSERT INTO listings (title, description, price) VALUES ('Second Listing', 'This is a description for the second listing', 2);
INSERT INTO listings (title, description, price) VALUES ('Third Listing', 'This is a description for the third listing', 0);
INSERT INTO listings (title, description, price) VALUES ('Fourth Listing', 'This is a description for the fourth listing', 0);