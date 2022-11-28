-- Lists all cities contained in the database `hbtn_0d_usa`
SELECT cities.id AS id, cities.name AS name, states.name AS name
  FROM cities
       LEFT OUTER JOIN states
  ON cities.state_id = states.id;
