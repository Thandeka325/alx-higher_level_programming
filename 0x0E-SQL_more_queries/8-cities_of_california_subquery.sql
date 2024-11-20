-- Script lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Results are sorted in ascending order by cities.id
-- List by not using `JOIN` keyword.
-- The database name will be passed as an argument of the mysql command.

USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
