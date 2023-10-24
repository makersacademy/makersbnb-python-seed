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
user_id int,
constraint fk_user foreign key(id)
    references users(id)
    on delete cascade
);

"""CREATE TABLE availability (
id SERIAL PRIMARY KEY,
date_not_available date,
status boolean,
requested_by_user_id int,
spaces_id
constraint fk_spaces foreign key(user_id)
    references spaces(user_id)
    on delete cascade
);"""