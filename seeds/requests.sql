CREATE TABLE requests(
    id SERIAL PRIMARY KEY,
    req_id int,
    space_id int,
    date_req text,
    stat text
);