-- Lists all records of the second_table table where the name column is not NULL, ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
