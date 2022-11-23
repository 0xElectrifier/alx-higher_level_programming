-- Lists the number of records with the same score in the table 'second_table' -- of the 'hbtn_0c_0' database in your MySQL server
SELECT score, COUNT(score) as number
  FROM `second_table`
  GROUP BY score
  ORDER BY number DESC;
