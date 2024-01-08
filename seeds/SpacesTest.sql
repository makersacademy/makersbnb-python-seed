DROP TABLE IF EXISTS Spaces;

CREATE TABLE Spaces(
    id SERIAL PRIMARY KEY,
    title text,
    space_description text,
    price float,
    daterange text,
    user_id int
);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title','This is some test description',65.75,'2024-01-12-2024-01-31',1);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title2','This is some test description',25.00,'2024-01-14-2024-01-29',1);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title3','This is some test description',135.50,'2024-01-12-2024-02-05',2);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title4','This is some test description',19.95,'2024-01-21-2024-01-31',2);

INSERT INTO Spaces(title,space_description,price,daterange,user_id) 
VALUES('Test Title5','This is some test description',1037.63,'2024-01-12-2024-01-19',3);