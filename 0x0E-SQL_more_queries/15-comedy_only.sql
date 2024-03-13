-- Lists all Comedy shows
USE hbtn_0d_tvshows;
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN genres ON genres.id = tv_show_genres.genre_id
WHERE genres.name = 'Comedy'
ORDER BY tv_shows.title;
