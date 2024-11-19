-- Script lists all records of the table `second_table`
-- Results displays both the score and the name (in this order).
-- Records ordered by score (top first)
-- The database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table
ORDER BY score DESC;
