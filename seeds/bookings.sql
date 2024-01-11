DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id INTEGER NOT NULL, -- which space is booked
    user_id INTEGER NOT NULL, -- id of user who booked space
    date DATE NOT NULL, -- date of booking
    price INTEGER NOT NULL -- price
);


-- availability management; if an entry is in the bookings table, it is no longer available
INSERT INTO bookings (space_id, user_id, date, price) VALUES
(1, 2, '2023-05-15', 120),
(1, 1, '2023-05-16', 120),
(2, 1, '2023-05-17', 95),
(3, 1, '2023-05-18', 110),
(4, 1, '2023-05-19', 140);