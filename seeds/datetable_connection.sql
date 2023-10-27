DROP TABLE IF EXISTS dates;

CREATE TABLE dates (
	id text primary key,
	spaceId text references spaces(id),
	date text,
	isAvailable BOOLEAN
);