-- Lists all cities of California in the database hbtn_0d_usa without JOIN
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities, states WHERE states.id = cities.state_id AND states.name = 'California' ORDER BY cities.id ASC;
