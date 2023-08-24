-- list all comedy shows
-- tv_genres contains only one record where name = Comedy
-- Each record should display tv_shows.title
-- sorted in asc by show title
-- use only one SELECT  statement

SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id

INNER JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
WHERE tg.name = "Comedy"
ORDER BY ts.title ASC;
