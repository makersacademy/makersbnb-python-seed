DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE IF NOT EXISTS listings (
    id SERIAL PRIMARY KEY,
    listing_name VARCHAR(255),
    listing_description VARCHAR(255),
    listing_price FLOAT,
    user_id INTEGER,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

INSERT INTO users (username, email, password) VALUES ('user1', 'user1email@example.com', 'password1');
INSERT INTO users (username, email, password) VALUES ('user2', 'user2email@example.com', 'password2');
INSERT INTO users (username, email, password) VALUES ('user3', 'user3email@example.com', 'password3');
INSERT INTO users (username, email, password) VALUES ('user4', 'user4email@example.com', 'password4');
INSERT INTO users (username, email, password) VALUES ('user5', 'user5email@example.com', 'password5');
INSERT INTO users (username, email, password) VALUES ('user6', 'user6email@example.com', 'password6');
INSERT INTO users (username, email, password) VALUES ('user7', 'user7email@example.com', 'password7');
INSERT INTO users (username, email, password) VALUES ('user8', 'user8email@example.com', 'password8');
INSERT INTO users (username, email, password) VALUES ('user9', 'user9email@example.com', 'password9');
INSERT INTO users (username, email, password) VALUES ('user10', 'user10email@example.com', 'password10');


INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Cozy Cottage', 'A charming cottage for a peaceful retreat', 99.99, 1);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Beachfront Villa', 'Enjoy stunning ocean views in this luxury villa', 249.95, 2);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Mountain Chalet', 'Experience the beauty of the mountains in this cozy chalet', 149.99, 3);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('City Apartment', 'Convenient urban living in the heart of the city', 89.49, 4);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Lakefront Cabin', 'Rustic cabin on the tranquil shores of the lake', 124.50, 5);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Seaside Bungalow', 'Relax in a charming bungalow by the sea', 199.99, 6);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Luxury Resort Suite', 'Indulge in luxury at this 5-star resort suite', 499.95, 7);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Countryside Retreat', 'Escape to the peaceful countryside in this cottage', 79.99, 8);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Historic Mansion', 'Step back in time at this historic mansion', 349.99, 9);
INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('Riverside Cabin', 'Cozy cabin with a river view, perfect for fishing', 109.75, 10);
