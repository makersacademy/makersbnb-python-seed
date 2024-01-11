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