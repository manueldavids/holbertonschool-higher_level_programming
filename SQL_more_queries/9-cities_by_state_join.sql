-- Script to list all cities with their states using JOIN
-- This script displays cities.id - cities.name - states.name

-- Select cities with their states using JOIN
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id;
