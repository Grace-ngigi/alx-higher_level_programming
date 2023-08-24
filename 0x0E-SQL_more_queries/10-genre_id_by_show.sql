-- lists all shows that have at lest one genre linked
-- results sorted in ascending order by tv_shows.title
-- and tv_show_genres.genre_id
-- use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
