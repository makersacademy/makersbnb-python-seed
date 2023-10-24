DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Spaces;
DROP TABLE IF EXISTS Dates;

CREATE TABLE Users (
user_id SERIAL PRIMARY KEY,
username text,
password varchar(255),
email varchar(255),
phone_number int,
);

CREATE TABLE Spaces (
user_id SERIAL PRIMARY KEY,
name text,
description text,
price-per-night, int,
);

user_id int,
constraint fk_user foreign key(user_id)
    references Users(id)
    on delete cascade

CREATE TABLE Availability (
space_id SERIAL PRIMARY KEY,
date-not-available date)
;

