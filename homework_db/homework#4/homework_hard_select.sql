SELECT COUNT(performer_id), genre.title_genre
  FROM genre_performer
 INNER JOIN genre ON genre_performer.genre_id = genre.genre_id
 GROUP BY title_genre;
 
SELECT COUNT(track_list_id)
  FROM track_list
  JOIN album ON track_list.album_id = album.album_id
 WHERE year_of_release BETWEEN 2019 and 2020;
 
SELECT AVG(track_list.duration), album.title_album
  FROM album
 INNER JOIN track_list ON track_list.album_id = album.album_id
 GROUP BY title_album;
 
SELECT DISTINCT performer.name, performer_id
  FROM performer
EXCEPT
SELECT performer.name, performer_album.performer_id
  FROM performer_album
  JOIN album ON performer_album.album_id = album.album_id
  JOIN performer ON performer.performer_id = performer_album.performer_id
 WHERE year_of_release = 2020;
 
SELECT DISTINCT collection.collection_title
  FROM performer_album
  JOIN track_list ON track_list.album_id = performer_album.album_id
  JOIN collection_track_list ON collection_track_list.track_list_id = track_list.track_list_id
  JOIN collection ON collection.collection_id = collection_track_list.collection_id
 WHERE performer_id = 10;
 
SELECT DISTINCT(album.title_album)
  FROM album
  JOIN performer_album ON performer_album.album_id = album.album_id
  JOIN genre_performer ON performer_album.performer_id = genre_performer.performer_id
 GROUP BY album.album_id, genre_performer.performer_id
HAVING COUNT(genre_id) > 1;
 
SELECT title_track
  FROM track_list
  LEFT JOIN collection_track_list
    ON track_list.track_list_id = collection_track_list.track_list_id
 WHERE collection_track_list.track_list_id IS NULL;
 
SELECT performer.name
  FROM performer
  JOIN performer_album ON performer_album.performer_id = performer.performer_id
  JOIN album ON album.album_id = performer_album.album_id
  JOIN track_list ON track_list.album_id = album.album_id
 WHERE track_list.duration = (SELECT MIN(duration) 
							    FROM track_list);
					
SELECT album.title_album
  FROM album
  JOIN track_list ON track_list.album_id = album.album_id
 GROUP BY album.album_id
HAVING COUNT(track_list_id) = (SELECT COUNT(track_list_id)
							     FROM track_list
							    GROUP BY album_id
							    ORDER BY 1
							    LIMIT 1);
					

					
