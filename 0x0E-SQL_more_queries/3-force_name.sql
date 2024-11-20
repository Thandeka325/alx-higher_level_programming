-- Script creates the table force_name.
-- The database name will be passed as an argument of the mysql command.
-- If the table force_name already exists, script does not fail.

CREATE TABLE IF NOT EXISTS force_name (
	id INT, 
	name VARCHAR(256) NOT NULL
);
