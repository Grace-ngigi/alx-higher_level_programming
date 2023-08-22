-- lists all cities of California fron db hbtn_0d_usa
-- result sorted in ascending order by cities.id
-- not allowed to use join
SELECT id, name FROM cities WHERE state_id IN 
(SELECT id FROM states WHERE name = "California")
ORDER BY cities.id ASC;
