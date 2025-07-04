-- Script to list all cities of California using subquery
-- This script finds cities where state_id matches California's id

-- Select cities of California using subquery
SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
