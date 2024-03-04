DROP TABLE IF EXISTS "user";
DROP SEQUENCE IF EXISTS user_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO "user" (name, password, email) VALUES ('Maria', 'Password', 'maria@gmail.com');
INSERT INTO "user" (name, password, email) VALUES ('Aakash', 'P*ssword', 'Aakash@outllok.com');
INSERT INTO "user" (name, password, email) VALUES ('Reeva', 'Pass1234', 'Reeva@yahoo.com');
INSERT INTO "user" (name, password, email) VALUES ('Jess', '1234Passw','Jess@hotmail.com');
INSERT INTO "user" (name, password, email) VALUES ('George', '**Passwo','George@gmail.com');
