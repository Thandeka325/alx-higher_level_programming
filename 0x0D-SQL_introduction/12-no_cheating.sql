-- Script updates the score of Bob to 10 in the table second_table.
-- Updates without using Bob’s id value, only the name field.
-- The database name will be passed as an argument of the mysql command

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
