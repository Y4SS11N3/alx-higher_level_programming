-- Lists all shows with at least one genre linked in hbtn_0d_tvshows
USE hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
