-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
  SELECT tv_show_genres.genre_id
  FROM tv_show_genres
  JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
  WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
