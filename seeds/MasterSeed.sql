CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    passw VARCHAR(255)
);

CREATE TABLE Spaces(
    id SERIAL PRIMARY KEY,
    title text,
    space_description text,
    price float,
    daterange text,
    user_id int
);

CREATE TABLE requests(
    req_id int,
    space_id int,
    date_req date,
    stat text,
    constraint fk_spaces foreign key(space_id)
    references spaces(id)
    on delete cascade,
    constraint fk_users foreign key(req_id)
    references users(id)
    on delete cascade
);


