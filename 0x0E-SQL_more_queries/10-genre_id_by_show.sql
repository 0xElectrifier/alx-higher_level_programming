-- Lists all shows contained in `hbtn_0d_tvshows` that have at least
-- one genre linked.
-- Using `hbtn_0d_tvshows` Database
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
  FROM tv_show_genres
       INNER JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
 WHERE tv_show_genres.genre_id > 0
 ORDER BY title, genre_id;
