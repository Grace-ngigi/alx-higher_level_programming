-- list all genres not linked to show DEXTER
-- record should display tv_genres.name
-- results sorted in asc order by genre name
-- use a max of two SELECT statements

SELECT DISTINCT tg.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id

INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE tg.name NOT IN
(
    SELECT name FROM tv_genres AS tg
    INNER JOIN tv_show_genres As tsg
    ON tg.id = tsg.genre_id

    INNER JOIN tv_shows AS ts
    ON tsg.show_id = ts.id
    WHERE ts.title = "Dexter"
)
ORDER BY tg.name ASC;
