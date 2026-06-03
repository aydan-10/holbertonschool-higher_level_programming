-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Records display: genre - number_of_shows
-- Results sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
