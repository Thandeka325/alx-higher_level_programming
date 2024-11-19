-- Script creates a table second_table in the database hbtn_0c_0, with multiple rows.
-- second_table description: `id` INT, `name' VARCHAR(256), `score` INT
-- If the table second_table already exists, script does not fail.
-- Creates a table without using SELCT and SHOW statements

CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'ALEX', 3),
(3, 'BOB', 14),
(4, 'George', 8);