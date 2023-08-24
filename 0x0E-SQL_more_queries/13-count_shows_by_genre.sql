-- list all genres and display the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- first column must be called genre
-- second column must be called number_of_shows
-- dont display a genre that doesnt have any shows linked
-- sorted in DESC order by number of shows linked
-- use only one SELECT statement

SELECT g.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON g.id = s.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
