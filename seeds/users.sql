DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS user_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email text, password text);

INSERT INTO users (email, password) VALUES ('test-email-1', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42');
INSERT INTO users (email, password) VALUES ('test-email-2', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2');
INSERT INTO users (email, password) VALUES ('test-email-3', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600');
