DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS user_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email text, password text);

INSERT INTO users (email, password) VALUES ('test-email-1', 'test-password-1');
INSERT INTO users (email, password) VALUES ('test-email-2', 'test-password-2');
INSERT INTO users (email, password) VALUES ('test-email-3', 'test-password-3');
