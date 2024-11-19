-- Script creates a table called first_table in the specified database.
-- Creates a table without using SELECT or SHOW statements
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, script will not fail
-- first_table description: id INT name VARCHAR(256)

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
