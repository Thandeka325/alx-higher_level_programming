-- Script displays the max temperature of each state.
-- Ordered by State name.

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
