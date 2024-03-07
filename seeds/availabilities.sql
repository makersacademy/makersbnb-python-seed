DROP TABLE IF EXISTS availabilities CASCADE;


CREATE TABLE availabilities (
  id SERIAL PRIMARY KEY,
  availability_from DATE,
  availability_to DATE,
  space_id INT,
  constraint fk_space foreign key(space_id) references spaces(id) ON DELETE CASCADE
);


INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-10-12', '2024-10-25', 1);
INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-05-21', '2024-06-01', 3);
INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-11-02', '2024-12-02', 4);
INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES ('2024-06-10', '2024-06-28', 2);