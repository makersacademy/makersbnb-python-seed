DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS availability ;

CREATE TABLE users (
id SERIAL PRIMARY KEY,
username varchar(255),
password varchar(255),
name text,
email varchar(255),
phone_number text
);

CREATE TABLE spaces (
id SERIAL PRIMARY KEY,
name text,
description text,
price_per_night numeric (7,2),
host_id int,
constraint fk_user foreign key(host_id)
    references users(id)

);

CREATE TABLE availability (
id SERIAL PRIMARY KEY,
date_not_available date,
approved text,
requested_by_user_id int,
spaces_id int,
constraint fk_spaces foreign key(spaces_id)
    references spaces(id)

);

INSERT INTO users (name, username, password, email, phone_number) VALUES ('Naomi Bloggs', 'Silvakippy369','782993a','Macicman@hotmail.com','01214960879');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Beata Ekkebert', 'Tomantning1789','A4$N61s','hir_ufizaxe52@yahoo.com','07700900186');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Rohese Clarity','Vegetebuck360','j=95J6','duha-gudedo63@outlook.com','01154960210');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Adolfo Dalit', 'Draffbrot1708','yuZY020#','jamixi_fajo87@yahoo.com','07700900191');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Apolónia Caelius', 'Mentalves26','XRy#14H6', 'rofenen-eya82@aol.com','07700900625');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Basu Eugenijus', 'Ajje04Mome','v9Q/l3~2', 'pizuye-xini98@aol.com','01314960681');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Inna Avital', 'Jockoman10245','^%41h6zW', 'reda-pajaru16@gmail.com','07700900485');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Anouk Verissimus', 'Bicornlian166',';628MGo', 'dox_epefize62@mail.com','03069990479');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Filipa Jyoti', 'Tiradepi280','uF#L6$89', 'gisuta-damo55@hotmail.com','07700900200');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Silas Narmer', 'Vaultynius39','PLd969;W', 'tule_piceyi54@yahoo.com','07700900239');
INSERT INTO users (name, username, password, email, phone_number) VALUES ('Cornelio Rozenn', 'Jossja0104','Zq07O0X', 'yaloki_saro39@aol.com','01214978789');

INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Mill Lodge', 'This large town is located near the coast and has a futuristic look.  It is best-known for its haunted house, a tumultuous history, and for being the home of a famous painter.  Also, there are all sorts of old artifacts still lying around the area.', 00000.00, 1);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('River View', 'This large town is located in the hills and has a rustic atmosphere.  It is best-known for its diverse population.  Also, rumor has it that many of the towns citizens are involved in some sort of secret project.', 00025.20, 1);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Melvins House', 'This small town is located in the desert and looks very modern.  It is best-known for the nearby military base.  Also, there are all sorts of old artifacts still lying around the area.', 01200.00, 1);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('The Old Vicarage', 'This large town is located by a lake and has a rustic atmosphere.  It is best-known for its haunted house.  Also, there are all sorts of old artifacts still lying around the area.', 00023.00, 3);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Black End', 'This moderate-sized town is located near the coast and looks very modern.  It is best-known for its beautiful park.  Also, rumor has it that the inhabitants are hiding something.', 00500.00, 4);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Primroselands', 'This large town is located in a valley and has a fairytale-like look to it.  It is best-known for its beautiful park, its autumn festival, and for being the home of a famous sculptor.  Also, rumor has it that the inhabitants are hiding something.', 00060.70, 2);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Firlands', 'This moderate-sized town is located in the hills and looks quite old.  It is best-known for its theater.  Also, there are all sorts of old artifacts still lying around the area.', 00123.00, 2);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('The Firs', 'This moderate-sized town is located in the desert and looks very old-fashioned.  It is best-known for its diverse population.  Also, rumor has it that a treasure is hidden somewhere in the town.', 00834.10, 5);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Sunny End', 'This large town is located in the mountains and has a rustic atmosphere.  It is best-known for a tumultuous history.  Also, rumor has it that the inhabitants may not be entirely human.', 10030.02, 5);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Middleton House', 'This moderate-sized town is located in a valley and has a rustic atmosphere.  It is best-known for a tumultuous history and its diverse population.  Also, rumor has it that the inhabitants are hiding something.', 00100.40, 7);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Newport Lodge', 'This small town is located by a lake and looks very old-fashioned.  It is best-known for its fine dining and for being the home of a famous painter.  Also, strange objects are occasionally seen in the sky.', 00020.70, 6);

INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2023-10-24', 'approved', 3, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2021-02-24', 'denied', 2, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2026-06-24', 'unavailable', 6, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2009-01-24', 'pending', 7, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2015-11-24', 'approved', 7, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2022-12-24', 'denied', 1, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2025-04-24', 'unavailable', 3, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2023-02-24', 'pending', 7, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2023-08-24', 'denied', 2, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2027-04-24', 'pending', 8, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES ('2023-09-24', 'approved', 9, 1);

