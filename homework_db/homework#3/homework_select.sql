SELECT title_album, year_of_release
  FROM album
 WHERE year_of_release = 2018;
 
SELECT title_track, duration
  FROM track_list
 WHERE duration = (SELECT MAX(duration)
				     FROM track_list);
					 
SELECT title_track
  FROM track_list
 WHERE duration > 210;
 
SELECT collection_title
  FROM collection
 WHERE year_of_release BETWEEN 2018 AND 2020;
 
SELECT name
  FROM performer
 WHERE name NOT LIKE '% %';
 
SELECT title_track
  FROM track_list
 WHERE title_track LIKE '% мой%' OR 
 		title_track LIKE '% my%' OR
		 title_track LIKE 'Мой%' OR
		  title_track LIKE 'My%';