-- Script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Results are sorted in ascending order by show title.

SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT title FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
