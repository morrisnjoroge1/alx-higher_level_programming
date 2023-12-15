-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, AVG(temperature) AS avg_temperature
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temperature DESC
LIMIT 3;
