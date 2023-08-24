-- list all genres of the show Dexter
-- tv_shows contains only one record where title = Dexter
-- Each row should display tv_genres.name
-- sorted in ASC order by genre name
-- use only one SELECT statement

SELECT tg.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id

INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY tg.name ASC;
