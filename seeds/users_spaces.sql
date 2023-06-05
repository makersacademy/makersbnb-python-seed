DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spaces;

DROP SEQUENCE IF EXISTS users_id_seq;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name text,
    last_name text,
    password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    title text,
    description text,
    price money,
    date_range date,
    -- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


