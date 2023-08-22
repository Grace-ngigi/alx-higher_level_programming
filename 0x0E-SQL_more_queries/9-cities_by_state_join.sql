-- lists all cities contained in db hbtn_0d_usa
-- each record displays cities.id - cities.name -states.name
-- results sorted by cities.id asc
-- only use one SELECT

SELECT city.id, city.name, state.name FROM cities AS city
INNER JOIN states AS state ON city.state_id = state.id
ORDER BY city.id ASC;
