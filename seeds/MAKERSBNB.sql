DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS availability ;

CREATE TABLE users (
id SERIAL PRIMARY KEY,
username varchar(255),
password varchar(255),
email varchar(255),
phone_number text
);

CREATE TABLE spaces (
id SERIAL PRIMARY KEY,
name text,
description text,
price_per_night numeric (5,2),
host_id int,
constraint fk_user foreign key(host_id)
    references users(id)
    on delete cascade
);

CREATE TABLE availability (
id SERIAL PRIMARY KEY,
date_not_available date,
approved boolean,
requested_by_user_id int,
spaces_id int,
constraint fk_spaces foreign key(spaces_id)
    references spaces(id)
    on delete cascade
);

INSERT INTO users (username, password, email, phone_number) VALUES ('Magicman','782993a','Macicman@hotmail.com','01214960879');
INSERT INTO users (username, password, email, phone_number) VALUES ('Beata Ekkebert','"A4$N61s','hir_ufizaxe52@yahoo.com','07700900186');
INSERT INTO users (username, password, email, phone_number) VALUES ('Rohese Clarity','"j=95J6"','duha-gudedo63@outlook.com','01154960210');
INSERT INTO users (username, password, email, phone_number) VALUES ('Adolfo Dalit','yuZY020#','jamixi_fajo87@yahoo.com','07700900191');
INSERT INTO users (username, password, email, phone_number) VALUES ('Apolónia Caelius','XRy#14H6','rofenen-eya82@aol.com','07700900625');
INSERT INTO users (username, password, email, phone_number) VALUES ('Basu Eugenijus','v9Q/l3~2','pizuye-xini98@aol.com','01314960681');
INSERT INTO users (username, password, email, phone_number) VALUES ('Inna Avital','^%41h6zW','reda-pajaru16@gmail.com','07700900485');
INSERT INTO users (username, password, email, phone_number) VALUES ('Anouk Verissimus',';6{28MGo','dox_epefize62@mail.com','03069990479');
INSERT INTO users (username, password, email, phone_number) VALUES ('Filipa Jyoti','uF#L6$89','gisuta-damo55@hotmail.com','07700900200');
INSERT INTO users (username, password, email, phone_number) VALUES ('Silas Narmer','PLd969;W','tule_piceyi54@yahoo.com','07700900239');
INSERT INTO users (username, password, email, phone_number) VALUES ('Cornelio Rozenn','Zq07O0)X','yaloki_saro39@aol.com','01214978789');

INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Mill Lodge', '', 00000.00, 1);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('River View', '', 00025.20, 1);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Melvins House', '', 01200.00, 1);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('The Old Vicarage', '', 00023.00, 3);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Black End', '', 00500.00, 4);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Primroselands', '', 00060.70, 2);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Firlands', '', 00123.00, 2);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('The Firs', '', 00834.10, 5);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Sunny End', '', 10030.02, 5);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Middleton House', '', 00100.40, 7);
INSERT INTO spaces (name, description, price_per_night, host_id) VALUES ('Newport Lodge', '', 00020.70, 6);

INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2023-10-24, false, 3, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2021-02-24, false, 2, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2026-06-24, true, 6, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2009-01-24, false, 7, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2015-11-24, true, 7, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2022-12-24, true, 1, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2025-04-24, false, 3, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2023-02-24, true, 7, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2023-08-24, false, 2, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2027-04-24, true, 8, 1);
INSERT INTO availability (date_not_available, approved, requested_by_user_id, spaces_id) VALUES (2023-09-24, false, 9, 1);