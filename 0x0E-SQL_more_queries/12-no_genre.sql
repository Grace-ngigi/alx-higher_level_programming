-- list all shows
-- display tv_shows.title - tv_show_genres.genre_id
-- sorted in ASC order by tv_show.title and tv_show_genres.genre.id
-- use only one select statement

SELECT shw.title, genre.genre_id
FROM tv_shows AS shw
LEFT JOIN tv_show_genres AS genre
ON shw.id = genre.show_id
WHERE genre.genre_id IS NULL
ORDER BY shw.title, genre.genre_id;
