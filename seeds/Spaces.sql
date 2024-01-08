CREATE TABLE Spaces(
    id SERIAL PRIMARY KEY,
    title text,
    space_description text,
    price float,
    daterange text,
    user_id int
);