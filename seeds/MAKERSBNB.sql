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
    references spaces(host_id)
    on delete cascade
);