DROP TABLE IF EXISTS spaces;

create table spaces (
	id TEXT PRIMARY KEY,
	name TEXT,
	ownerId TEXT references users(id),
	description text,
	price TEXT,
	startDate TEXT,
	endDate text
);