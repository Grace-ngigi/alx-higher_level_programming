-- list all shows and all genres linked to that show
-- if show doesnt have genre, display NULL in genre column
-- record should display tv_shows.title - tv_genres.name
-- use only one SELECT statement

SELECT ts.title, tg.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
ORDER by ts.title, tg.name ASC;
