# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

user_table_create = ("""CREATE TABLE users (
user_id varchar, 
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar, 
PRIMARY KEY (user_id)
)
""")

artist_table_create = ("""CREATE TABLE artists (
artist_id varchar NOT NULL, 
name varchar, 
location varchar, 
latitude numeric, 
longitude numeric, 
PRIMARY KEY (artist_id)
)
""")

# artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric)")

song_table_create = ("""CREATE TABLE songs (
song_id varchar, 
title varchar, 
artist_id varchar NOT NULL, 
year int, 
duration numeric, 
PRIMARY KEY (song_id), 
CONSTRAINT fk_artists_artist_id FOREIGN KEY (artist_id) 
REFERENCES artists (artist_id) 
ON UPDATE CASCADE ON DELETE CASCADE
)
""")

# song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year int, duration numeric)")

time_table_create = ("""CREATE TABLE time (
start_time timestamp, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int, 
PRIMARY KEY (start_time)
)
""")

# time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time time, hour int, day int, week int, month int, year int, weekday varchar)")

songplay_table_create = ("""CREATE TABLE songplays (
songplay_id SERIAL, 
start_time timestamp, 
user_id varchar, 
level varchar, 
song_id varchar, 
artist_id varchar, 
session_id int, 
location varchar, 
user_agent varchar, 
PRIMARY KEY (songplay_id), 
CONSTRAINT fk_time_start_time FOREIGN KEY (start_time) 
REFERENCES time (start_time) 
ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_users_user_id FOREIGN KEY (user_id) 
REFERENCES users (user_id) 
ON UPDATE CASCADE ON DELETE CASCADE, 
CONSTRAINT fk_songs_song_id FOREIGN KEY (song_id) 
REFERENCES songs (song_id) 
ON UPDATE CASCADE ON DELETE CASCADE, 
CONSTRAINT fk_artists_artist_id FOREIGN KEY (artist_id) 
REFERENCES artists (artist_id) 
ON UPDATE CASCADE ON DELETE CASCADE
)
""")

# songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id serial primary key, start_time time, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)")


# user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar, PRIMARY KEY (user_id))")

# user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar)")


# INSERT RECORDS

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO NOTHING;
""")

# user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
#  ON CONFLICT (user_id) DO UPDATE SET level = exclude.level;
#  """)

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = (""" SELECT songs.song_id as songid, songs.artist_id as artistid FROM artists JOIN songs ON artists.artist_id = songs.artist_id WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s ORDER BY songs.song_id ASC """)

# song_select = ("""SELECT songs.song_id as songid, songs.artist_id as artistid FROM songs INNER JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = %s AND artist.name = %s AND songs.duration = %s OrDER BY songs.song_id ASC
# """)

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]  
               
# create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
# drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# DROP TABLES

# songplay_table_drop = "DROP TABLE IF EXISTS songplays";
# user_table_drop = "DROP TABLE IF EXISTS users";
# song_table_drop = "DROP TABLE IF EXISTS songs";
# artist_table_drop = "DROP TABLE IF EXISTS artists";
# time_table_drop = "DROP TABLE IF EXISTS time";

# CREATE TABLES

#  songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL, start_time timestamp NOT NULL, user_id varchar NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar, PRIMARY KEY (songplay_id), FOREIGN KEY (user_id) REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (song_id) REFERENCES songs (song_id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (artist_id) REFERENCES artists (artist_id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (start_time) REFERENCES time (start_time) ON UPDATE CASCADE ON DELETE CASCADE)")

# user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar, PRIMARY KEY (user_id))")

# song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year int, duration numeric, PRIMARY KEY (song_id), FOREIGN KEY(artist_id) REFERENCES artists(artist_id) ON UPDATE CASCADE ON DELETE CASCADE)")

# artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric, PRIMARY KEY (artist_id))")

# time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int, PRIMARY KEY (start_time))")

# INSERT RECORDS

# songplay_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")

# user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;")

# song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;")

# artist_table_insert = ("INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;")


# time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;")

# FIND SONGS

# song_select = """
# SELECT s.song_id AS songig, s.artist_id AS artistid FROM songs s INNER JOIN artists a ON s.artist_id = a.artist_id WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s ORDER BY s.song_id ASC)
#"""

# QUERY LISTS

# create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
# drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]