-- Lists all cities contained in the database hbtn_0d_usa.
-- Lists all rows of a particular column in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON state.id = cities.state_idORDER BY cities.id;
