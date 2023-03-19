DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS performer CASCADE;
DROP TABLE IF EXISTS genre_performer CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS performer_album CASCADE;
DROP TABLE IF EXISTS track_list CASCADE;
DROP TABLE IF EXISTS collection CASCADE;
DROP TABLE IF EXISTS collection_track_list CASCADE;

CREATE TABLE genre
	   (genre_id serial PRIMARY KEY,
	   title_genre varchar(64) NOT NULL UNIQUE);

CREATE TABLE performer
	   (performer_id serial PRIMARY KEY,
	   name text NOT NULL UNIQUE);

CREATE TABLE genre_performer
	   (genre_id int REFERENCES genre(genre_id),
	   performer_id int REFERENCES performer(performer_id),
	   CONSTRAINT genre_performer_pkey PRIMARY KEY (genre_id, performer_id));

CREATE TABLE album
	   (album_id serial PRIMARY KEY,
	   title_album varchar(64) NOT NULL,
	   year_of_release int NOT NULL CHECK(year_of_release > 1950));

CREATE TABLE performer_album
	   (performer_id int REFERENCES performer(performer_id),
	   album_id int REFERENCES album(album_id),
	   CONSTRAINT performer_album_pkey PRIMARY KEY (performer_id, album_id));

CREATE TABLE track_list
	   (track_list_id serial PRIMARY KEY,
	   title_track text NOT NULL,
	   duration int NOT NULL,
	   album_id int REFERENCES album(album_id));

CREATE TABLE collection
	   (collection_id serial PRIMARY KEY,
	   collection_title varchar(64) NOT NULL,
	   year_of_release int NOT NULL CHECK(year_of_release > 1950));

CREATE TABLE collection_track_list
	   (collection_id int REFERENCES collection(collection_id),
	   track_list_id int REFERENCES track_list(track_list_id),
	   CONSTRAINT collection_track_list_pkey PRIMARY KEY (collection_id, track_list_id));
