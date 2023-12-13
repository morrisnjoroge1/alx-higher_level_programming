-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- result should display: the score, number of records for this score with the label number
-- list should be sorted by the number of records (descending)

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
GROUP BY score ORDER BY number DESC, score;
