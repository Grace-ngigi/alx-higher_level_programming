-- list all shows in the db
-- each record should display tv_title - tv_show_genres.genre_id
-- sorted in asc bytv_shows.title and tv_show_genres.genre_id
-- if show does not have genre display null
-- use only one select statement

SELECT shw.title, genre.genre_id
FROM tv_shows AS shw
LEFT JOIN tv_show_genres  AS genre
ON shw.id = genre.show_id
ORDER BY shw.title, genre.genre_id;
