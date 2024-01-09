
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
	user_name text,
	email text,
	password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
	address text,
	name text,
    price int,
    image_path text,
    description text,
    date_added date,
    date_available date,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id)
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date_booked text,
    user_id int,
    space_id int,
    constraint fk_user foreign key(user_id) references users(id),
    constraint fk_space foreign key(space_id) references spaces(id)
);


INSERT INTO users (user_name, email, password) VALUES
('Lil kim', 'femalerappers@femalerappers.com', 'apassword1@A'),
('Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
('Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*');


INSERT INTO spaces (address, name, price, image_path, description, date_added, date_available, user_id) VALUES
('123 Horse Lane', 'Wild horses', 56, '/images/lilkim.jpg', 'A light, warm, and modern space for a gathering.', '2020-10-22', '2024-06-22', 1),
('5 Zoo lane', 'Zootropolis', 124, '/images/zoos.jpg', 'A nice warm bed amongst the animals', '2019-08-21', '2024-04-10', 2),
('789 Starlight Street', 'Celestial Haven', 72, '/images/celestial_haven.jpg', 'Experience the tranquility under the stars in this celestial haven.', '2022-02-08', '2024-02-01', 3),
('101 Mountain View', 'Mountain Hideaway', 110, '/images/mountain_hideaway.jpg', 'Escape to the serene mountains and enjoy the breathtaking views.', '2023-01-17', '2024-05-15', 2),
('222 Beachfront Road', 'Ocean Paradise Villa', 150, '/images/ocean_paradise.jpg', 'Relax by the beach in this luxurious oceanfront villa.', '2022-11-30', '2024-10-12', 1),
('333 Skyline Tower', 'Cityscape Loft', 95, '/images/cityscape_loft.jpg', 'A modern loft with stunning views of the city skyline.', '2020-12-03', '2024-08-20', 3),
('444 Lakeside Drive', 'Tranquil Lake Cottage', 80, '/images/lake_cottage.jpg', 'Escape to this cozy cottage by the lake for a peaceful retreat.', '2021-09-25', '2024-09-18', 2);

INSERT INTO bookings (date_booked, user_id, space_id) VALUES
('2024-02-01', 1, 3),
('2024-04-10', 1, 2),
('2024-05-15', 2, 4),
('2024-06-22', 2, 1),
('2024-08-20', 2, 6),
('2024-09-18', 3, 7),
('2024-10-12', 3, 5);

