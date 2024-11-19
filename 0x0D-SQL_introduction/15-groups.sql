-- Script lists the number of records with the same score in the table second_table.
-- The results display the score, and the number of records for this score with the label number.
-- The list is sorted by the number of records (descending).
-- The database name will be passed as an argument to the mysql command.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
