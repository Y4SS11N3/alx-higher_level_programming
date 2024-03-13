-- Lists all cities of California in the database hbtn_0d_usa without JOIN
SELECT cities.id, cities.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id ASC;
