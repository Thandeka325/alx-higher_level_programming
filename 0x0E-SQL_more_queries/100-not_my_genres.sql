-- Script uses the hbtn_0d_tvshows database to lists all genres not linked the show Dexter.
-- Results are sorted in ascending order by genre name.

SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT name FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
