DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS availability ;

CREATE TABLE users (
id SERIAL PRIMARY KEY,
username varchar(255),
password varchar(255),
email varchar(255),
phone_number int
);

CREATE TABLE spaces (
id SERIAL PRIMARY KEY,
name text,
description text,
price_per_night numeric,
spaces_user_id int
constraint fk_user foreign key(id)
    references users(id)
    on delete cascade
);

"""CREATE TABLE availability (
date_not_available date,
status boolean,
requested_by_user_id int,


constraint fk_space foreign key(space_id)
    references spaces(space_id)
    on delete cascade
);"""