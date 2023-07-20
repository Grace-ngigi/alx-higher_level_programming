-- Get the state_id for California from the states table using a subquery
SELECT id INTO @california_id FROM states WHERE name = 'California';

-- Fetch all cities of California using the state_id obtained from the subquery
SELECT * FROM cities WHERE state_id = @california_id ORDER BY id ASC;
