-- lists all shows and all genres linked to that show
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement

SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
