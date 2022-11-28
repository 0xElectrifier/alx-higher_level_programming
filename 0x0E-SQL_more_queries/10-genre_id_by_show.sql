-- Lists all shows contained in `hbtn_0d_tvshows` that have at least
-- one genre linked.
SELECT tv_shows.title as title, tv_show_genres.genre_id as genre_id
  FROM tv_show_genres
       INNER JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
 WHERE tv_show_genres.genre_id > 0
 ORDER BY title, genre_id;
