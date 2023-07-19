-- display  citites with highest temp between July and Aug
SELECT city, AVG(value) AS temperature
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY temperature DESC
LIMIT 3;

