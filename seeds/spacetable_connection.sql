DROP TABLE IF EXISTS spaces CASCADE;

create table spaces (
	id TEXT PRIMARY KEY,
	name TEXT,
	description TEXT,
	ownerId TEXT references users(id),
	startDate TEXT,
	endDate text
);

INSERT INTO spaces VALUES ('1', 'this is a name of a space', 'description', '4r8e9ujfoiuriej', '23-09-2025', '29-09-2025');
INSERT INTO spaces VALUES ('2', 'second space', 'description', '54y7r8euhi', '23-09-2025', '29-09-2025');