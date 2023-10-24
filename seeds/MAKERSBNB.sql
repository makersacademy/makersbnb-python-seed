DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Spaces;
DROP TABLE IF EXISTS Dates;

CREATE TABLE Users (
user_id SERIAL PRIMARY KEY,
username varchar(255),
password varchar(255),
email varchar(255),
phone_number int,
);

CREATE TABLE Spaces (
user_id SERIAL PRIMARY KEY,
space_id SERIAL PRIMARY KEY,
name text,
description text,
price_per_night, int,
);

user_id int,
constraint fk_user foreign key(user_id)
    references Users(user_id)
    on delete cascade

SELECT 
Users.user_id,
Users.username,
Users.email,
Users.phone_number,

Spaces.space_id,
Spaces.user_id,
Space.name,
Spaces.description,
Spaces.price_per_night,

FROM Users
    JOIN Spaces
    ON Users.user_id = Spaces.user_id;

CREATE TABLE Availability (
space_id SERIAL PRIMARY KEY,
date_not_available date,
approved boolean,
);

space_id int,
constraint fk_space foreign key(space_id)
    references Spaces(space_id)
    on delete cascade

SELECT 
Spaces.space_id,
Spaces.user_id,
Space.name,
Spaces.description,
Spaces.price_per_night,

Availability.space_id,
Availability.date_not_available,
Availability.approved,

FROM Spaces
    JOIN Availability
    ON Spaces.space_id = Availability.space_id;

