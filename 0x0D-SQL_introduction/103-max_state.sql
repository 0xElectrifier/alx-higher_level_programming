-- Imports the 'temperatures.sql' file and,
-- displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) as max_temp
  FROM `temperatures`
  GROUP BY `value`
  ORDER BY `state`;
