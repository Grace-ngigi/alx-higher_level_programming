-- display max temp of states,ordered by state
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
