-- LIsts all records of the table 'second_table' of the 'hbtn_0c_0' database
-- in your MySQL server
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
