-- group by score and order by number
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
