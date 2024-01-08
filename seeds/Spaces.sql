CREATE TABLE Spaces(
    id SERIAL PRIMARY KEY,
    title text,
    space_description text,
    price float,
    daterange text,
    user_id int
);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) VALUES (
    'Test Title','This is a test description',12.75,'2024/01/15-2024/01/31',1
);