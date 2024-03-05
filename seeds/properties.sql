DROP TABLE IF EXISTS properties cascade;
DROP SEQUENCE IF EXISTS properties_id_seq;

CREATE SEQUENCE IF NOT EXISTS properties_id_seq;
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT, 
    price INTEGER, 
    user_id INTEGER,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    booked_status BOOLEAN);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO properties (name, description, price, user_id, booked_status) VALUES ( 
    'Chestnut Eco Lodge Woodland Escape', 'House with garden', 101, 1, FALSE); 
INSERT INTO properties (name, description, price, user_id, booked_status) VALUES ( 
    'The Hazel Hide', 'Luxury Eco A-Frame Cabin', 240, 3, FALSE); 
INSERT INTO properties (name, description, price, user_id, booked_status) VALUES ( 
    'Entire Contemporary Barn', 'Barn in Essex', 550, 5, FALSE); 
INSERT INTO properties (name, description, price, user_id, booked_status) VALUES ( 
    'Coloc All Included Febvotte-Marat', 'Room in Tours', 463, 1, FALSE); 
INSERT INTO properties (name, description, price, user_id, booked_status) VALUES ( 
    '2RJ2- Hyper center.', 'Entire rental unit in Tours', 472, 4, TRUE); 